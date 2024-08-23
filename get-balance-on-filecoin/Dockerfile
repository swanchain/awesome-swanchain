# read the doc: https://docs.lagrangedao.org/lagrange-dao/getstarted/spaces/docker-spaces
# you will also find guides on how best to write your Dockerfile

FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .
EXPOSE 7860
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
