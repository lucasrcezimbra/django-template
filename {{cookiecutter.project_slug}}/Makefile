.PHONY: install dev lint deploy test dbseed

install:
        poetry install

dev:
        poetry run python manage.py runserver 0.0.0.0:8000

lint:
        poetry run pre-commit run --all-files

deploy:
        poetry run python manage.py migrate
        poetry run python manage.py collectstatic --noinput

test:
        poetry run pytest

dbseed:
        poetry run python manage.py loaddata initial_data
