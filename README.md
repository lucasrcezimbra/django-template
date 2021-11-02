# Django Template
[![Updates](https://pyup.io/repos/github/lucasrcezimbra/django-template/shield.svg)](https://pyup.io/repos/github/lucasrcezimbra/django-template/)

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
