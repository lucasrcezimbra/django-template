import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path().absolute()


def remove(path):
    (PROJECT_DIRECTORY / path).unlink()


if __name__ == "__main__":
    if "{{cookiecutter.api}}" == "No":
        remove("{{cookiecutter.project_slug}}/core/api.py")
        remove("{{cookiecutter.project_slug}}/core/tests/test_api.py")
    if "{{cookiecutter.api}}" != "Django Ninja CRUD":
        remove("{{cookiecutter.project_slug}}/core/tests/test_crud.py")

    if "{{cookiecutter.deploy}}" != "Docker":
        remove("Dockerfile")
        remove(".dockerignore")
    if "{{cookiecutter.deploy}}" != "Heroku":
        remove("Procfile")
    if "{{cookiecutter.deploy}}" != "Render":
        remove("render.yaml")

    if "{{cookiecutter.html}}" == "No":
        shutil.rmtree("{{cookiecutter.project_slug}}/core/templates/")
        remove("{{cookiecutter.project_slug}}/core/tests/test_view_index.py")
        remove("{{cookiecutter.project_slug}}/core/views.py")
        remove("{{cookiecutter.project_slug}}/users/views.py")

    if "{{cookiecutter.staticfiles}}" != "True":
        shutil.rmtree("{{cookiecutter.project_slug}}/static/")

    if "{{cookiecutter.database}}" != "PostgreSQL":
        remove("docker-compose.yml")

    if "{{cookiecutter.css}}" != "Bootstrap":
        remove("{{cookiecutter.project_slug}}/static/bootstrap.min.css")
        remove("{{cookiecutter.project_slug}}/static/bootstrap.min.js")
