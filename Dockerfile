FROM python:3.7-alpine

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install requirements
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

# copy application codebase
RUN mkdir /api
WORKDIR /api
COPY bouncer .

CMD python manage.py runserver 0.0.0.0:$PORT
