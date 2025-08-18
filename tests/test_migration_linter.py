DEFAULT_PROJECT = "api"


def test_django_migration_linter_included(cookies):
    result = cookies.bake()

    assert result.exit_code == 0

    with open(result.project / "pyproject.toml") as f:
        content = f.read()
        assert "django-migration-linter" in content


def test_django_migration_linter_in_installed_apps(cookies):
    result = cookies.bake()

    assert result.exit_code == 0

    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "django_migration_linter" in content


def test_makefile_includes_lintmigrations(cookies):
    result = cookies.bake()

    assert result.exit_code == 0

    with open(result.project / "Makefile") as f:
        content = f.read()
        assert "poetry run python manage.py lintmigrations" in content


def test_migration_linter_works_with_different_configurations(cookies):
    configurations = [
        {"database": "SQLite", "api": "No", "html": "No"},
        {"database": "PostgreSQL", "api": "Django Ninja", "html": "HTMX"},
        {"database": "PostgreSQL", "api": "Django Ninja CRUD", "html": "Default"},
    ]

    for config in configurations:
        result = cookies.bake(extra_context=config)
        assert result.exit_code == 0

        with open(result.project / "pyproject.toml") as f:
            content = f.read()
            assert "django-migration-linter" in content

        with open(result.project / "Makefile") as f:
            content = f.read()
            assert "poetry run python manage.py lintmigrations" in content

        with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
            content = f.read()
            assert "django_migration_linter" in content
