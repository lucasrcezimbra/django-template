# Django Template

An opinionated Django start project template.


## How to Use
```bash
pip install -U cookiecutter
cookiecutter https://github.com/lucasrcezimbra/django-template
```


## Features
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) to cast database URL to Django setting
- [django-extensions](https://github.com/django-extensions/django-extensions) for custom extensions for Django
- [docker](https://www.docker.com/) with [compose](https://github.com/docker/compose)
- [PostgreSQL](https://www.postgresql.org/) database
- [pytest-django](https://github.com/pytest-dev/pytest-django), [pytest-mock](https://github.com/pytest-dev/pytest-mock) and [models_bakery](https://github.com/model-bakers/model_bakery) for tests
- [python-decouple](https://github.com/henriquebastos/python-decouple) to organize settings and decouple from code

Optionals:
- [Heroku](https://www.heroku.com/) to deploy


## Tree
```
api
├── api
│   ├── asgi.py
│   ├── core
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── managers.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── index.html
│   │   ├── tests
│   │   │   ├── tests.py
│   │   │   └── test_view_index.py
│   │   └── views.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── contrib
│   ├── env-sample
│   └── secret_gen.py
├── docker-compose.yml
├── manage.py
├── Procfile
├── pytest.ini
├── README.md
├── requirements-dev.txt
└── requirements.txt
```


## Contribute
Contributions are welcome, feel free to suggest improvements.
