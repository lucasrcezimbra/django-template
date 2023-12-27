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
    if "{{cookiecutter.deploy}}" != "Heroku":
        remove("Procfile")
    if "{{cookiecutter.deploy}}" != "Render":
        remove("render.yaml")

    if "{{cookiecutter.html}}" == "No":
        shutil.rmtree("{{cookiecutter.project_slug}}/core/templates/")
        remove("{{cookiecutter.project_slug}}/core/views.py")
    if "{{cookiecutter.html}}" != "HTMX":
        remove("{{cookiecutter.project_slug}}/static/htmx.min.js.gz")

    if "{{cookiecutter.staticfiles}}" != "True":
        shutil.rmtree("{{cookiecutter.project_slug}}/static/")

    if "{{cookiecutter.database}}" != "PostgreSQL":
        remove("docker-compose.yml")
