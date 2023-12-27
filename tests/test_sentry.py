DEFAULT_PROJECT = "api"


def test_default_true(cookies):
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


def test_false(cookies):
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
