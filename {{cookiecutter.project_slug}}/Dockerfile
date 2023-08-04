FROM python:3.10

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install poetry
COPY poetry.lock pyproject.toml .
RUN python -m poetry install --no-root --without=dev

COPY . /app

CMD ["python", "-m", "poetry", "run", "gunicorn", "{{cookiecutter.project_slug}}.wsgi:application", "--bind", "0.0.0.0:8000"]
