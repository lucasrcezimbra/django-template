# Django Template

An opinionated Django start project template.


## How to Use
### Using Cruft (Recommended)
Cruft is compatible with Cookiecutter and is the recommended method because it
allows you to update the project with the latest template changes using
`cruft update`.

```bash
pip install cruft
cruft create https://github.com/lucasrcezimbra/django-template
cd <project_name>
git init
make install
git add .
git commit -m "Initial commit"
```

### Using Cookiecutter
```bash
pip install -U cookiecutter
cookiecutter https://github.com/lucasrcezimbra/django-template
cd <project_name>
git init
make install
git add .
git commit -m "Initial commit"
```


## Features
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) to cast database URL to Django setting
- [django-extensions](https://github.com/django-extensions/django-extensions) for custom extensions for Django
- [django-migration-linter](https://github.com/3YOURMIND/django-migration-linter) to detect backward incompatible migrations
- [docker](https://www.docker.com/) with [compose](https://github.com/docker/compose)
- [GitHub](https://github.com/) Actions for CI
- [Gunicorn](https://gunicorn.org/) as WSGI HTTP Server
- [PostgreSQL](https://www.postgresql.org/) database with connection pooling enabled
- [pre-commit](https://github.com/pre-commit/pre-commit) with
[black](https://github.com/psf/black),
[ruff](https://github.com/astral-sh/ruff),
[yamlfmt](https://github.com/google/yamlfmt),
[actionlint](https://github.com/rhysd/actionlint),
and [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
- [pytest-django](https://github.com/pytest-dev/pytest-django),
[pytest-mock](https://github.com/pytest-dev/pytest-mock),
[pytest-deadfixtures](https://github.com/jllorencetti/pytest-deadfixtures),
and [models_bakery](https://github.com/model-bakers/model_bakery) for tests
- [python-decouple](https://github.com/henriquebastos/python-decouple) to organize settings and decouple from code

Optionals:
- [Django](https://github.com/adamchainz/django-htmx) [HTMX](https://htmx.org/)
- [Django Ninja](https://github.com/vitalik/django-ninja) and [Django Ninja CRUD](https://github.com/hbakri/django-ninja-crud) to build APIs
- [djLint](https://github.com/djlint/djLint) and [djade](https://github.com/adamchainz/djade)
- [Dockerfile](https://www.docker.com/), [Heroku](https://www.heroku.com/) or [Render](https://render.com/) to deploy
- [Sentry](https://sentry.io/) for error tracking
- [WhiteNoise](https://github.com/evansd/whitenoise) to serve static files


### Tree
\*optionals
```shell
api
├── api
│   ├── asgi.py
│   ├── core
│   │   ├── admin.py
│   │   ├── api.py*
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── managers.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates*
│   │   │   └── index.html
│   │   ├── tests
│   │   │   ├── test_api.py*
│   │   │   ├── test_crud.py*
│   │   │   └── test_view_index.py*
│   │   └── views.py*
│   ├── __init__.py
│   ├── settings.py
│   ├── static*
│   │   └── htmx.min.js.gz
│   ├── urls.py
│   ├── users
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── managers.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests
│   │   │   └── test_users.py
│   │   └── views.py*
│   └── wsgi.py
├── contrib
│   ├── env-sample
│   └── secret_gen.py
├── docker-compose.yml*
├── Dockerfile*
├── .dockerignore*
├── .env
├── .github
│   ├── dependabot.yml
│   └── workflows
│       └── python-app.yml
├── .gitignore
├── manage.py
├── .pre-commit-config.yaml
├── Procfile*
├── pyproject.toml
├── README.md
└── render.yaml*
```


## Rationales
### Custom user model
> If you’re starting a new project, it’s highly recommended to set up a custom
> user model, even if the default User model is sufficient for you. This model
> behaves identically to the default user model, but you’ll be able to customize
> it in the future if the need arises

from https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project


### Custom user model in a isolated app
It's difficult to migrate the custom user model to a new app after the project
is created.

You may need to move your custom model to a new app to use app like
[django-tenants](https://github.com/django-tenants/django-tenants) and
[django-tenant-users](https://github.com/Corvia/django-tenant-users/).

To avoid these migration issues, the custom user model is created in an isolated
`users` app.



## Contribute
Contributions are welcome, feel free to suggest improvements.
