#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path().absolute()


def remove(path):
    (PROJECT_DIRECTORY / path).unlink()


if __name__ == "__main__":
    if "{{cookiecutter.deploy}}" != "Heroku":
        remove("Procfile")
    if "{{cookiecutter.api}}" == "No":
        remove("{{cookiecutter.project_slug}}/core/api.py")
        remove("{{cookiecutter.project_slug}}/core/tests/test_api.py")
    if "{{cookiecutter.deploy}}" != "Docker":
        remove("Dockerfile")
    if "{{cookiecutter.deploy}}" != "Render":
        remove("render.yaml")
    if "{{cookiecutter.api}}" != "Django Ninja CRUD":
        remove("{{cookiecutter.project_slug}}/core/tests/test_crud.py")
