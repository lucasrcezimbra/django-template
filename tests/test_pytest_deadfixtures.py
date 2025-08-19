DEFAULT_PROJECT = "api"


def test_pytest_deadfixtures_included(cookies):
    """Test that pytest-deadfixtures is included in dev dependencies."""
    result = cookies.bake()

    assert result.exit_code == 0

    with open(result.project / "pyproject.toml") as f:
        content = f.read()
        assert "pytest-deadfixtures" in content


def test_makefile_includes_pytest_deadfixtures(cookies):
    """Test that the lint command includes pytest --dead-fixtures."""
    result = cookies.bake()

    assert result.exit_code == 0

    with open(result.project / "Makefile") as f:
        content = f.read()
        assert "poetry run pytest --dead-fixtures" in content