FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY Pipfile /code/
COPY Pipfile.lock /code/
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --deploy --system

COPY . /code/
