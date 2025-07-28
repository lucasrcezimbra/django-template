.PHONY: install lint test

install:
	poetry install --no-root
	poetry run pre-commit install
	poetry run pre-commit install-hooks

lint:
	poetry run pre-commit run -a

test:
	poetry run pytest

test-generated:
	poetry run cookiecutter . --no-input database="SQLite" project_slug="test_project" css="No"
	cd test_project/ && make install
	cd test_project/ && make test
	cd test_project/ && git init && git add . && make lint
	rm -rf test_project/
