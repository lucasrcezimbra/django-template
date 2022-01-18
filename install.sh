#!/bin/bash

pip install django --upgrade \
    && django-admin startproject --template=https://github.com/lucasrcezimbra/django-template/archive/master.zip --name=Procfile,env-sample --extension=env,ini,txt,yml $PROJECT --exclude \
    && cd $PROJECT \
    && rm install.sh LICENSE README.md \
    && python -m venv .venv \
    && source .venv/bin/activate \
    && pip install -r requirements-dev.txt \
    && git init \
    && pre-commit install \
    && docker-compose up -d \
    && sleep 5 \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py runserver
