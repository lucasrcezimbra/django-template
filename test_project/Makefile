.DEFAULT_GOAL := dev
.PHONY: build dev install lint run test

build:
	poetry install
	poetry run python manage.py collectstatic --no-input
	poetry run python manage.py migrate

dev:
	
	docker compose up -d
	poetry run python manage.py migrate
	poetry run python manage.py runserver

install:
	
	docker compose up -d
	poetry install
	poetry run pre-commit install
	cp contrib/env-sample .env

lint:
	poetry run pre-commit run -a

lint-local:
	poetry run black --check .
	poetry run ruff check .

run:
	poetry run gunicorn test_project.wsgi:application

test:
	
	docker compose up -d
	poetry run pytest
