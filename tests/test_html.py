DEFAULT_PROJECT = "api"


def test_default(cookies):
    result = cookies.bake()

    core_app_path = result.project / DEFAULT_PROJECT / "core"
    users_app_path = result.project / DEFAULT_PROJECT / "users"
    assert (core_app_path / "templates" / "index.html").exists()
    assert (core_app_path / "views.py").exists()
    assert (users_app_path / "views.py").exists()
    assert not (result.project / DEFAULT_PROJECT / "static" / "htmx.min.js.gz").exists()

    with open(result.project / "pyproject.toml") as f:
        assert "django_htmx" not in f.read()

    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        assert "django_htmx" not in f.read()

    with open(core_app_path / "templates" / "index.html") as f:
        assert "{% static 'htmx.min.js.gz' %}" not in f.read()

    with open(result.project / ".pre-commit-config.yaml") as f:
        content = f.read()
        assert "djade" in content
        assert "djLint" in content


def test_no(cookies):
    result = cookies.bake(extra_context={"html": "No"})

    core_app_path = result.project / DEFAULT_PROJECT / "core"
    users_app_path = result.project / DEFAULT_PROJECT / "users"
    assert not (core_app_path / "templates").exists()
    assert not (core_app_path / "views.py").exists()
    assert not (users_app_path / "views.py").exists()
    assert not (core_app_path / "tests" / "test_view_index.py").exists()
    assert not (result.project / DEFAULT_PROJECT / "static" / "htmx.min.js.gz").exists()

    with open(result.project / "pyproject.toml") as f:
        assert "django_htmx" not in f.read()

    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        assert "django_htmx" not in f.read()

    with open(result.project / DEFAULT_PROJECT / "urls.py") as f:
        assert "index" not in f.read()

    with open(result.project / ".pre-commit-config.yaml") as f:
        content = f.read()
        assert "djade" not in content
        assert "djLint" not in content


def test_htmx(cookies):
    result = cookies.bake(extra_context={"html": "HTMX"})

    core_app_path = result.project / DEFAULT_PROJECT / "core"
    assert (core_app_path / "templates" / "index.html").exists()
    assert (core_app_path / "views.py").exists()
    assert (result.project / DEFAULT_PROJECT / "static" / "htmx.min.js.gz").exists()

    with open(result.project / "pyproject.toml") as f:
        assert "django-htmx =" in f.read()

    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "django_htmx" in content
        assert "django_htmx.middleware.HtmxMiddleware" in content

    with open(core_app_path / "templates" / "index.html") as f:
        assert "{% static 'htmx.min.js.gz' %}" in f.read()

    with open(result.project / ".pre-commit-config.yaml") as f:
        content = f.read()
        assert "djade" in content
        assert "djLint" in content
