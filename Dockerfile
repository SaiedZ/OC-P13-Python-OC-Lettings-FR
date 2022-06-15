# set the Base Image from which your image will be built on
FROM python:3.10-alpine
LABEL maintainer="Deias"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# copy the current directory in you local machine to /app in image
COPY . .

RUN apk update && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --no-cache-dir -r requirements.txt

# collect static files and migrate
RUN /py/bin/python manage.py collectstatic --noinput && \
    /py/bin/python manage.py migrate

EXPOSE 8000

ENV PATH="/py/bin:$PATH"

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "oc_lettings_site.wsgi:application"]

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT