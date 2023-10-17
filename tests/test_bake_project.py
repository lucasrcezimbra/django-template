from textwrap import dedent

DEFAULT_PROJECT = "api"


def test_bake_with_defaults(cookies):
    result = cookies.bake()

    assert result.project.isdir()
    assert result.exit_code == 0
    assert result.exception is None

    found_toplevel_files = {f.basename for f in result.project.listdir()}
    assert "pyproject.toml" in found_toplevel_files
    assert "api" in found_toplevel_files


def test_sentry_default_true(cookies):
    result = cookies.bake()

    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "import sentry_sdk" in content
        assert 'SENTRY_DSN = config("SENTRY_DSN", default=None)' in content

    with open(result.project / "contrib" / "env-sample") as f:
        assert "SENTRY_DSN=" in f.read()

    with open(result.project / ".env") as f:
        assert "SENTRY_DSN=" in f.read()

    with open(result.project / "pyproject.toml") as f:
        assert 'sentry-sdk = {extras = ["django"], version = "' in f.read()


def test_sentry_false(cookies):
    result = cookies.bake(extra_context={"use_sentry": False})

    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "import sentry_sdk" not in content
        assert 'SENTRY_DSN = config("SENTRY_DSN", default=None)' not in content

    with open(result.project / "contrib" / "env-sample") as f:
        assert "SENTRY_DSN=" not in f.read()

    with open(result.project / ".env") as f:
        assert "SENTRY_DSN=" not in f.read()

    with open(result.project / "pyproject.toml") as f:
        assert 'sentry-sdk = {extras = ["django"], version = "' not in f.read()


def test_staticfiles_default_true(cookies):
    result = cookies.bake()

    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "django.contrib.staticfiles" in content
        assert "whitenoise.middleware.WhiteNoiseMiddleware" in content
        assert (
            dedent(
                """\
                STATIC_ROOT = BASE_DIR / "staticfiles"
                STATIC_URL = "/static/"
                STORAGES = {
                    "staticfiles": {
                        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
                    },
                }"""
            )
            in content
        )

    with open(result.project / "pyproject.toml") as f:
        assert 'whitenoise = {extras = ["brotli"], version = "' in f.read()


def test_staticfiles_false(cookies):
    result = cookies.bake(extra_context={"staticfiles": False})

    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "staticfiles" not in content
        assert "whitenoise" not in content
        assert "STATIC_ROOT" not in content
        assert "STATIC_URL" not in content
        assert "STORAGES" not in content

    with open(result.project / "pyproject.toml") as f:
        assert "whitenoise" not in f.read()


def test_no_deploy(cookies):
    result = cookies.bake()
    found_toplevel_files = {f.basename for f in result.project.listdir()}

    assert "Procfile" not in found_toplevel_files
    assert "Dockerfile" not in found_toplevel_files
    with open(result.project / "README.md") as f:
        content = f.read()
        assert "## Deploy" not in content
        assert "heroku" not in content


def test_deploy_docker(cookies):
    result = cookies.bake(extra_context={"deploy": "Docker"})
    found_toplevel_files = {f.basename for f in result.project.listdir()}

    assert "Procfile" not in found_toplevel_files
    assert "Dockerfile" in found_toplevel_files
    with open(result.project / "README.md") as f:
        content = f.read()
        assert "## Deploy" not in content
        assert "heroku" not in content


def test_deploy_heroku(cookies):
    result = cookies.bake(extra_context={"deploy": "Heroku"})
    found_toplevel_files = {f.basename for f in result.project.listdir()}

    assert "Procfile" in found_toplevel_files
    assert "Dockerfile" not in found_toplevel_files
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


def test_github_username(cookies):
    result = cookies.bake(extra_context={"github_username": "my_custom_username"})

    with open(result.project / "README.md") as f:
        assert "git clone git@github.com:my_custom_username/api.git" in f.read()
