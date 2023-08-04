# Django Template

An opinionated Django start project template that uses:
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) to cast database URL to Django setting
- [django-extensions](https://github.com/django-extensions/django-extensions) for custom extensions for Django
- [docker](https://www.docker.com/) with [compose](https://github.com/docker/compose)
- [PostgreSQL](https://www.postgresql.org/) database
- [pytest-django](https://github.com/pytest-dev/pytest-django), [pytest-mock](https://github.com/pytest-dev/pytest-mock) and [models_bakery](https://github.com/model-bakers/model_bakery) for tests
- [python-decouple](https://github.com/henriquebastos/python-decouple) to organize settings and decouple from code

Optionals:
- [Heroku](https://www.heroku.com/) to deploy


## How to Use
```bash
pip install -U cookiecutter
cookiecutter https://github.com/lucasrcezimbra/django-template
```


## Contribute
Contributions are welcome, feel free to suggest improvements.


## TODOs
- [ ] If not Heroku remove Procfile
- [ ] Update this README
