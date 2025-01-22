# syntax=docker/dockerfile:1.2
FROM python:latest
# put you docker configuration here
FROM python:3.10
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "challenge.api:app", "--host", "0.0.0.0", "--port", "8080"]
