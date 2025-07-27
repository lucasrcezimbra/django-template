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
```

### Using Cookiecutter
```bash
pip install -U cookiecutter
cookiecutter https://github.com/lucasrcezimbra/django-template
```


## Features
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) to cast database URL to Django setting
- [django-extensions](https://github.com/django-extensions/django-extensions) for custom extensions for Django
- [docker](https://www.docker.com/) with [compose](https://github.com/docker/compose)
- [GitHub](https://github.com/) Actions for CI
- [Gunicorn](https://gunicorn.org/) as WSGI HTTP Server
- [PostgreSQL](https://www.postgresql.org/) database
- [pre-commit](https://github.com/pre-commit/pre-commit) with
[black](https://github.com/psf/black),
[ruff](https://github.com/astral-sh/ruff),
[yamlfmt](https://github.com/google/yamlfmt),
[actionlint](https://github.com/rhysd/actionlint),
and [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
- [pytest-django](https://github.com/pytest-dev/pytest-django),
[pytest-mock](https://github.com/pytest-dev/pytest-mock),
and [models_bakery](https://github.com/model-bakers/model_bakery) for tests
- [python-decouple](https://github.com/henriquebastos/python-decouple) to organize settings and decouple from code
- Child project triggering on release - automatically triggers child projects to update with latest template changes

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


## Child Project Updates

This template includes an automated mechanism to trigger child projects (projects created from this template) to update when a new release is published.

### How it works

1. When a new release is created in this repository, the "Trigger Child Projects" workflow runs
2. The workflow sends repository dispatch events to configured child repositories
3. Child repositories can listen for these events and automatically run `cruft update` to get the latest template changes

### Setup for Repository Maintainers

To configure which child repositories should be triggered:

1. Set up the `CHILD_REPOSITORIES` repository variable with a comma-separated list of repositories (format: `owner/repo`)
   - Example: `user1/my-project,user2/another-project`

2. Create a `CHILD_PROJECTS_TOKEN` secret with a GitHub personal access token that has `repo` scope for the child repositories

### Setup for Child Projects

Child projects need to add a workflow to listen for repository dispatch events:

```yaml
name: Update from Template
on:
  repository_dispatch:
    types: [cruft_update]

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install cruft
        run: pip install cruft
      - name: Update from template
        run: cruft update --skip-apply-ask
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          title: "Update from template ${{ github.event.client_payload.template_version }}"
          body: |
            Automated update from django-template version ${{ github.event.client_payload.template_version }}

            Template URL: ${{ github.event.client_payload.template_url }}
          branch: template-update
```


## Contribute
Contributions are welcome, feel free to suggest improvements.
