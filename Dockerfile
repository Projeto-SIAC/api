FROM python:3.6-alpine

RUN apk --update add \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev

RUN pip install pipenv --upgrade

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --dev --deploy --system
