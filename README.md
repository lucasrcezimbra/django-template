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
- [Gunicorn](https://gunicorn.org/) as WSGI HTTP Server
- [PostgreSQL](https://www.postgresql.org/) database
- [pre-commit](https://github.com/pre-commit/pre-commit) with
[bandit](https://github.com/PyCQA/bandit),
[black](https://github.com/psf/black),
[flake8](https://github.com/pycqa/flake8),
[isort](https://github.com/timothycrosley/isort),
and [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
- [pytest-django](https://github.com/pytest-dev/pytest-django),
[pytest-mock](https://github.com/pytest-dev/pytest-mock),
and [models_bakery](https://github.com/model-bakers/model_bakery) for tests
- [python-decouple](https://github.com/henriquebastos/python-decouple) to organize settings and decouple from code

Optionals:
- [Dockerfile](https://www.docker.com/)
- [Django Ninja](https://github.com/vitalik/django-ninja) and [Django Ninja CRUD](https://github.com/hbakri/django-ninja-crud) to build APIs
- [Heroku](https://www.heroku.com/) to deploy


### Tree
```
api
├── api
│   ├── asgi.py
│   ├── core
│   │   ├── admin.py
│   │   ├── api.py
│   │   ├── apps.py
│   │   ├── facades
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── managers.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── index.html
│   │   ├── tests
│   │   │   ├── test_api.py
│   │   │   ├── test_crud.py
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
├── Dockerfile
├── manage.py
├── Procfile
├── pyproject.toml
└── README.md
```


## Contribute
Contributions are welcome, feel free to suggest improvements.
