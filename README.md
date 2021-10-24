# Django Template
[![Updates](https://pyup.io/repos/github/lucasrcezimbra/django-template/shield.svg)](https://pyup.io/repos/github/lucasrcezimbra/django-template/)

An opinionated Django start project template that uses:
- [python-decouple](https://github.com/henriquebastos/python-decouple) to organize settings and decouple from code
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) to cast database URL to Django setting
- [django-extensions](https://github.com/django-extensions/django-extensions) for custom extensions for Django
- [pytest-django](https://github.com/pytest-dev/pytest-django) and [pytest-mock](https://github.com/pytest-dev/pytest-mock) for tests
- [Heroku](https://www.heroku.com/) to deploy


## How to Use
```bash
pip install django
PROJECT=myproject \
        && django-admin startproject --template=https://github.com/lucasrcezimbra/django-template/archive/master.zip --name=Procfile --extension=env,ini,txt $PROJECT \
        && cd $PROJECT \
        && python -m venv .venv \
        && source .venv/bin/activate \
        && pip install -r requirements-dev.txt \
        && git init \
        && pre-commit install \
        && python manage.py makemigrations \
        && python manage.py migrate \
        && python manage.py runserver
```

## Deploy
```bash
PROJECT=myproject \
        && git add . \
        && git commit -m 'First blood' \
        && heroku create $PROJECT \
        && heroku config:set DEBUG=True SECRET_KEY=`python contrib/secret_gen.py` ALLOWED_HOSTS='.herokuapp.com'\
        && git push heroku master
```

## Contribute

Contributions are welcome, feel free to suggest improvements.


##

[ ~ Dependencies scanned by PyUp.io ~ ]
