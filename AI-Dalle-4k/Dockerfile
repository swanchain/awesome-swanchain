FROM python:3.9
ENV DEBIAN_FRONTEND=noninteractive
ADD requirements.txt /
ADD app.py /
# Pre requirements
RUN pip install --no-cache-dir -r /requirements.txt
EXPOSE 9999

ENTRYPOINT ["python", "/app.py"]
