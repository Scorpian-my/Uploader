FROM python:3.10

RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip && pip install rubpy

RUN python /app/bot.py
