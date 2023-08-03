# {{ cookiecutter.project_slug }}


## Installation
```bash
git clone git@github.com:lucasrcezimbra/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
docker-compose up -d
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
cp contrib/env-sample .env
```

### Test
```bash
pytest
```

### Run
```bash
python manage.py migrate
python manage.py runserver
```


## Deploy
```bash
heroku create {{ cookiecutter.project_slug }}
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set DEBUG=True SECRET_KEY=`python contrib/secret_gen.py` ALLOWED_HOSTS="*"
git push heroku master
```
