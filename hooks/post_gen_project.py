#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path().absolute()


def remove(path):
    abs_path = PROJECT_DIRECTORY / path
    abs_path.unlink()


if __name__ == "__main__":
    if not {{cookiecutter.use_heroku}}:
        remove("Procfile")
    if not {{cookiecutter.use_django_ninja}}:
        remove("{{cookiecutter.project_slug}}/core/api.py")
        remove("{{cookiecutter.project_slug}}/core/tests/test_api.py")
