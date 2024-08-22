from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
database = []
class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    database.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    return database

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in database:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.get("/")
def read_root():
    return {"ping": "pong"}