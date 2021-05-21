FROM python:3.9.0-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt \
&&  mkdir /app

COPY app /app

WORKDIR /app

CMD ["python","main.py"]

