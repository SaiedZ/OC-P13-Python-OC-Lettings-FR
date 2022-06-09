# set the Base Image from which your image will be built on
FROM python:3.10
LABEL maintainer="Deias"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# create a directory called flask-circleci in root.
# This directory will contain the code which currently resides in
RUN mkdir /django-app
# make /django-app the working directory
# copy the current directory in you local machine to /django-app in your image
COPY . /django-app
WORKDIR /django-app

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt

ENV PATH="/py/bin:$PATH"
