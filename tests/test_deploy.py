from textwrap import dedent


def test_no(cookies):
    result = cookies.bake()
    found_toplevel_files = {f.basename for f in result.project.listdir()}

    assert "Procfile" not in found_toplevel_files
    assert "Dockerfile" not in found_toplevel_files
    assert ".dockerignore" not in found_toplevel_files
    assert "render.yaml" not in found_toplevel_files
    with open(result.project / "README.md") as f:
        content = f.read()
        assert "## Deploy" not in content
        assert "heroku" not in content


def test_docker(cookies):
    result = cookies.bake(extra_context={"deploy": "Docker"})
    found_toplevel_files = {f.basename for f in result.project.listdir()}

    assert "Procfile" not in found_toplevel_files
    assert "render.yaml" not in found_toplevel_files
    assert "Dockerfile" in found_toplevel_files
    assert ".dockerignore" in found_toplevel_files
    with open(result.project / "README.md") as f:
        content = f.read()
        assert "## Deploy" not in content
        assert "heroku" not in content


def test_heroku(cookies):
    result = cookies.bake(extra_context={"deploy": "Heroku"})
    found_toplevel_files = {f.basename for f in result.project.listdir()}

    assert "Dockerfile" not in found_toplevel_files
    assert ".dockerignore" not in found_toplevel_files
    assert "render.yaml" not in found_toplevel_files
    assert "Procfile" in found_toplevel_files
    with open(result.project / "README.md") as f:
        assert (
            dedent(
                """\
                    ## Deploy
                    ```bash
                    heroku create api
                    heroku addons:create heroku-postgresql:hobby-dev
                    heroku config:set DEBUG=True SECRET_KEY=`python contrib/secret_gen.py` ALLOWED_HOSTS="*"
                    git push heroku master
                    ```"""
            )
            in f.read()
        )


def test_render(cookies):
    result = cookies.bake(extra_context={"deploy": "Render"})
    found_toplevel_files = {f.basename for f in result.project.listdir()}

    assert "Procfile" not in found_toplevel_files
    assert "Dockerfile" not in found_toplevel_files
    assert ".dockerignore" not in found_toplevel_files
    assert "render.yaml" in found_toplevel_files
    with open(result.project / "render.yaml") as f:
        assert f.read() == dedent(
            """\
            databases:
              - name: api
                databaseName: api
                user: api
                plan: free

            services:
              - type: web
                name: api
                plan: free
                runtime: python
                buildCommand: "poetry install && poetry run python manage.py collectstatic && poetry run python manage.py migrate"
                startCommand: "poetry run gunicorn api.wsgi:application"
                envVars:
                  - key: DATABASE_URL
                    fromDatabase:
                      name: api
                      property: connectionString
                  - key: SECRET_KEY
                    generateValue: true
                  - key: WEB_CONCURRENCY
                    value: 4
                  - key: ALLOWED_HOSTS
                    value: api.onrender.com
                  - key: PYTHON_VERSION
                    value: 3.13.5
                  - key: POETRY_VERSION
                    value: 1.6.1
                    """
        )
