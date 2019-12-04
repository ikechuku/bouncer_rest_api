FROM python:3.7-alpine

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependency for psycopg2
# install psycopg2 packages
# delete the added virtual package added to 'world'
RUN apk update \
    && apk add --virtual build-deps gcc python-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install requirements
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

# copy application codebase
RUN mkdir /app
WORKDIR /app
COPY bouncer .

CMD python manage.py runserver 0.0.0.0:8000
