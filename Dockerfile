FROM python:3

WORKDIR /app

COPY ./requirements.txt .

RUN pip install greenlet
RUN pip install -r requirements.txt

COPY . .