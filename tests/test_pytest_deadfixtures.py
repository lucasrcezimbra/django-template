DEFAULT_PROJECT = "api"


def test_pytest_deadfixtures_included(cookies):
    result = cookies.bake()

    assert result.exit_code == 0

    with open(result.project / "pyproject.toml") as f:
        content = f.read()
        assert "pytest-deadfixtures" in content


def test_makefile_includes_pytest_deadfixtures(cookies):
    result = cookies.bake()

    assert result.exit_code == 0

    with open(result.project / "Makefile") as f:
        content = f.read()
        assert "poetry run pytest --dead-fixtures" in content
