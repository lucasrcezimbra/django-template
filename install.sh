#!/bin/bash

pip install django --upgrade \
    && django-admin startproject --template=https://github.com/lucasrcezimbra/django-template/archive/master.zip --name=Procfile,env-sample --extension=env,ini,txt,yml,md-tpl $PROJECT --exclude \
    && cd $PROJECT \
    && rm install.sh LICENSE README.md \
    && mv README.md-tpl README.md \
    && docker-compose up -d \
    && python -m venv .venv \
    && source .venv/bin/activate \
    && pip install -r requirements-dev.txt \
    && git init \
    && pre-commit install \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py runserver
