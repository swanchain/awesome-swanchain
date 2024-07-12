from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from transformers import pipeline

app = FastAPI()

pipe_flan = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/infer_t5")
def t5(input):
    output = pipe_flan(input)
    return {"output": output[0]["generated_text"]}

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def index() -> FileResponse:
    return FileResponse(path="/app/static/index.html", media_type="text/html")