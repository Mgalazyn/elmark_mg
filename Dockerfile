FROM python:3.10-alpine3.17

ENV PYTHONUNBUFFERED 1
RUN mkdir /my_task
WORKDIR /my_task

COPY . /my_task/

RUN pip install -r requirements.txt

