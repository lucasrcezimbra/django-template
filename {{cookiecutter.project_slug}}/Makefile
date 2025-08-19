.DEFAULT_GOAL := dev
.PHONY: build dev install lint run test update-template

build:
	poetry install
	poetry run python manage.py collectstatic --no-input
	poetry run python manage.py migrate

dev:
	{% if cookiecutter.database == 'PostgreSQL' %}
	docker compose up -d
	{% endif -%}
	poetry run python manage.py migrate
	poetry run python manage.py runserver

install:
	{% if cookiecutter.database == 'PostgreSQL' %}
	docker compose up -d
	{% endif -%}
	poetry install
	poetry run pre-commit install
	cp contrib/env-sample .env

lint:
	poetry run pre-commit run -a
	poetry run python manage.py lintmigrations
	poetry run pytest --dead-fixtures

run:
	poetry run gunicorn {{ cookiecutter.project_slug }}.wsgi:application

test:
	{% if cookiecutter.database == 'PostgreSQL' %}
	docker compose up -d
	{% endif -%}
	poetry run pytest

update-template:
	poetry run cruft update --skip-apply-ask
