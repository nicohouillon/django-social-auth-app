FROM python:3.13.0a2-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN mkdir /web
RUN mkdir /web/django_social_auth_app

WORKDIR /web

COPY ./requirements.txt /web/
COPY ./manage.py /web/

RUN pip install -r requirements.txt

COPY ./django_social_auth_app /web/django_social_auth_app

ENV PORT=8000                             \
    ALLOWED_HOSTS=localhost               \
    PREFIX_URL=

CMD python manage.py runserver 0.0.0.0:$PORT
