def test_default_logging_config(cookies):
    """Test that the default logging configuration is present and properly configured."""
    result = cookies.bake()

    assert result.project.isdir()
    assert result.exit_code == 0
    assert result.exception is None

    # Read the generated settings.py file
    settings_file = result.project / "api" / "settings.py"
    with open(settings_file) as f:
        settings_content = f.read()

    # Check that JsonFormatter import is present
    assert "from pythonjsonlogger.json import JsonFormatter" in settings_content

    # Check that LOGGING configuration is present
    assert "LOGGING = {" in settings_content
    assert '"version": 1' in settings_content
    assert '"disable_existing_loggers": False' in settings_content

    # Check formatters are present
    assert '"formatters": {' in settings_content
    assert '"structured"' in settings_content
    assert '"plaintext"' in settings_content

    # Check that structured formatter uses JsonFormatter
    assert '"()": JsonFormatter,' in settings_content

    # Check handlers are present
    assert '"handlers": {' in settings_content
    assert '"console"' in settings_content
    assert '"class": "logging.StreamHandler"' in settings_content

    # Check loggers are present
    assert '"loggers": {' in settings_content
    assert '"django"' in settings_content
    assert '"api"' in settings_content  # project slug

    # Check that environment variable configuration is used
    assert 'LOG_LEVEL = config("LOG_LEVEL"' in settings_content
    assert 'config("LOG_FORMATTER"' in settings_content

    # Check that DJANGO_LOG_LEVEL is not used anymore
    assert 'config("DJANGO_LOG_LEVEL"' not in settings_content


def test_logging_config_with_custom_project_slug(cookies):
    """Test logging configuration with custom project slug."""
    result = cookies.bake(extra_context={"project_slug": "my_project"})

    settings_file = result.project / "my_project" / "settings.py"
    with open(settings_file) as f:
        settings_content = f.read()

    # Check that the project-specific logger uses the correct slug
    assert '"my_project": {' in settings_content


def test_logging_config_formatter_selection(cookies):
    """Test that formatter selection is based on LOG_FORMATTER environment variable."""
    result = cookies.bake()

    settings_file = result.project / "api" / "settings.py"
    with open(settings_file) as f:
        settings_content = f.read()

    # Check that formatter selection uses LOG_FORMATTER environment variable
    assert (
        '"formatter": config("LOG_FORMATTER", default="structured")' in settings_content
    )


def test_logging_config_without_staticfiles(cookies):
    """Test that logging configuration is present even when staticfiles is disabled."""
    result = cookies.bake(extra_context={"staticfiles": False})

    settings_file = result.project / "api" / "settings.py"
    with open(settings_file) as f:
        settings_content = f.read()

    # Ensure staticfiles config is not present
    assert "STATICFILES" not in settings_content
    assert "django.contrib.staticfiles" not in settings_content

    # But logging configuration should still be present
    assert "LOGGING = {" in settings_content
    assert '"version": 1' in settings_content
    assert '"api": {' in settings_content  # project slug logger


def test_python_json_logger_dependency(cookies):
    """Test that python-json-logger dependency is included in pyproject.toml."""
    result = cookies.bake()

    pyproject_file = result.project / "pyproject.toml"
    with open(pyproject_file) as f:
        pyproject_content = f.read()

    # Check that python-json-logger dependency is present
    assert "python-json-logger" in pyproject_content
