FROM python:3.7-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependency for psycopg2
# Install psycopg2 package
# Delete the added virtual package added to 'world'
# Make curl available for running commands
RUN apk update \
    && apk add --virtual build-deps gcc python-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps \
    && apk add curl \
    && rm -rf /var/cache/apk/*

# Install requirements
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

# copy application codebase
RUN mkdir /app
WORKDIR /app
COPY bouncer .
