# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV API_KEY 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

# install dependencies
RUN apk update
RUN apk add git
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .