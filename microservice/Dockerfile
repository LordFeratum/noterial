FROM python:3.6-alpine

RUN apk --no-cache add \
      ca-certificates \
      openssl-dev \
      libffi-dev \
      libc-dev \
      gcc \
      postgresql-dev\
      musl-dev

ENV PYTHONPATH=/app/src/
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . /app/
WORKDIR /app

ARG ENV=local

RUN pip install -r /app/requirements/$ENV.txt
