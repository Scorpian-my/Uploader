FROM python:3.10


RUN pip install --upgrade pip && pip install rubpy

RUN python3 bot.py
