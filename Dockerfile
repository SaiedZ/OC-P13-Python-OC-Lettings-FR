# set the Base Image from which your image will be built on
FROM python:3.10-alpine
LABEL maintainer="Deias"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# copy the current directory in you local machine to /app in image
COPY . .

    # install psycopg2 and packages
RUN pip install --upgrade pip && \
    apk add --virtual build-essential gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    pip install psycopg2 && \
    pip install --no-cache-dir -r requirements.txt && \
    # collect static files and migrate
    python manage.py collectstatic --noinput && \
    python manage.py migrate

EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "oc_lettings_site.wsgi:application"]

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT