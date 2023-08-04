# {{ cookiecutter.project_name }}


## Installation
```bash
git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
docker-compose up -d
poetry install
poetry run pre-commit install
cp contrib/env-sample .env
```

### Test
```bash
poetry run pytest
```

### Run
```bash
poetry run python manage.py migrate
poetry run manage.py runserver
```
{% if cookiecutter.use_heroku %}


## Deploy
```bash
heroku create {{ cookiecutter.project_slug }}
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set DEBUG=True SECRET_KEY=`python contrib/secret_gen.py` ALLOWED_HOSTS="*"
git push heroku master
```
{% endif %}