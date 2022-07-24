# Django Template

An opinionated Django start project template that uses:
- [python-decouple](https://github.com/henriquebastos/python-decouple) to organize settings and decouple from code
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) to cast database URL to Django setting
- [django-extensions](https://github.com/django-extensions/django-extensions) for custom extensions for Django
- [pytest-django](https://github.com/pytest-dev/pytest-django), [pytest-mock](https://github.com/pytest-dev/pytest-mock) and [models_bakery](https://github.com/model-bakers/model_bakery) for tests
- [Heroku](https://www.heroku.com/) to deploy
- [PostgreSQL](https://www.postgresql.org/) database
- [docker](https://www.docker.com/) with [compose](https://github.com/docker/compose)


## How to Use
```bash
export PROJECT=my_project_name \
    && curl -o- https://raw.githubusercontent.com/lucasrcezimbra/django-template/master/install.sh | bash \
    && cd $PROJECT
```

## Contribute

Contributions are welcome, feel free to suggest improvements.
