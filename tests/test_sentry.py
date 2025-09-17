DEFAULT_PROJECT = "api"


def test_default_true(cookies):
    result = cookies.bake()

    with open(result.project_path / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "import sentry_sdk" in content
        assert "from sentry_sdk.integrations.django import DjangoIntegration" in content
        assert 'SENTRY_DSN = config("SENTRY_DSN", default=None)' in content
        assert "DjangoIntegration(cache_spans=True)" in content
        # Check frontend context processor
        assert "core.context_processors.sentry_context" in content

    with open(result.project_path / "contrib" / "env-sample") as f:
        assert "SENTRY_DSN=" in f.read()

    with open(result.project_path / ".env") as f:
        assert "SENTRY_DSN=" in f.read()

    with open(result.project_path / "pyproject.toml") as f:
        assert 'sentry-sdk = {extras = ["django"], version = "' in f.read()

    # Check frontend integration
    core_app_path = result.project_path / DEFAULT_PROJECT / "core"

    # Check context processor file exists
    assert (core_app_path / "context_processors.py").exists()

    with open(core_app_path / "context_processors.py") as f:
        content = f.read()
        assert "def sentry_context(request):" in content
        assert "SENTRY_DSN" in content
        assert "SENTRY_ENV" in content

    # Check base.html includes Sentry script
    with open(core_app_path / "templates" / "base.html") as f:
        content = f.read()
        assert "browser.sentry-cdn.com" in content
        assert "Sentry.init" in content
        assert "{{ SENTRY_DSN" in content


def test_false(cookies):
    result = cookies.bake(extra_context={"use_sentry": False})

    with open(result.project_path / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "import sentry_sdk" not in content
        assert (
            "from sentry_sdk.integrations.django import DjangoIntegration"
            not in content
        )
        assert 'SENTRY_DSN = config("SENTRY_DSN", default=None)' not in content
        # Check context processor is not included
        assert "core.context_processors.sentry_context" not in content

    with open(result.project_path / "contrib" / "env-sample") as f:
        assert "SENTRY_DSN=" not in f.read()

    with open(result.project_path / ".env") as f:
        assert "SENTRY_DSN=" not in f.read()

    with open(result.project_path / "pyproject.toml") as f:
        assert 'sentry-sdk = {extras = ["django"], version = "' not in f.read()

    # Check frontend integration is not included
    core_app_path = result.project_path / DEFAULT_PROJECT / "core"

    # Check context processor file doesn't exist
    assert not (core_app_path / "context_processors.py").exists()

    # Check base.html doesn't include Sentry script
    with open(core_app_path / "templates" / "base.html") as f:
        content = f.read()
        assert "browser.sentry-cdn.com" not in content
        assert "Sentry.init" not in content
