.PHONY: install lint test

install:
	poetry install

lint:
	poetry run pre-commit run -a

test:
	poetry run pytest
