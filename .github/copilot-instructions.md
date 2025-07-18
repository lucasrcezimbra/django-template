# Copilot Instructions for Django Template

## Project Overview

This is a **Cookiecutter template** for generating opinionated Django projects. It's not a Django application itself, but rather a template that generates Django applications with various configurable features.

## Terminology

To avoid confusion when working on issues, PRs, and documentation:
- **Root, cookiecutter, and generator project**: refers to the cookiecutter project that lives in the root folder and generates the Django project
- **Generated and Django project**: refers to the project generated by cookiecutter

## Key Concepts

### Template Structure
- **Root directory**: Contains the Cookiecutter configuration and template files
- **`{{cookiecutter.project_slug}}/`**: The actual Django project template that gets generated
- **`cookiecutter.json`**: Configuration file defining template variables and options
- **`tests/`**: Test suite for validating template generation

### Usage and Updates
- **Cruft (Recommended)**: Cruft is compatible with Cookiecutter and is the recommended method for creating projects because it allows updating the generated project with the latest template changes using `cruft update`
- **Cookiecutter**: Standard method for generating projects, but doesn't support updates

### Template Variables
The main configuration options in `cookiecutter.json`:
- `project_name`: Name of the generated project (default: "API")
- `project_slug`: URL-friendly version of project name
- `github_username`: GitHub username for repository URLs
- `database`: Choose between "PostgreSQL" or "SQLite"
- `api`: API framework options ("No", "Django Ninja", "Django Ninja CRUD")
- `html`: HTML approach ("Default", "HTMX", "No")
- `css`: CSS framework ("Bootstrap", "No")
- `deploy`: Deployment options ("No", "Docker", "Heroku", "Render")
- `use_sentry`: Boolean for Sentry error tracking
- `staticfiles`: Boolean for static file handling

## Generated Project Features

The template creates Django projects with:

### Core Features (Always Included)
- Custom User model in isolated `users` app
- Django Extensions for development utilities
- Python Decouple for settings management
- dj-database-url for database configuration
- Pre-commit hooks with Black, Ruff, yamlfmt, actionlint
- pytest-django, pytest-mock, and model_bakery for testing
- GitHub Actions CI/CD pipeline

### Optional Features (Based on Configuration)
- **API**: Django Ninja for REST APIs with CRUD operations
- **HTML**: HTMX for dynamic frontend interactions
- **CSS**: Bootstrap styling
- **Database**: PostgreSQL (with Docker) or SQLite
- **Deployment**: Docker, Heroku, or Render configurations
- **Monitoring**: Sentry integration for error tracking
- **Static Files**: WhiteNoise for serving static files

## File Structure Patterns

### Template Files
- Files in `{{cookiecutter.project_slug}}/` use Jinja2 templating
- Conditional files use `{% if cookiecutter.option %}` blocks
- Variable substitution uses `{{ cookiecutter.variable_name }}`

### Generated Project Structure
```
project_name/
├── project_slug/           # Main Django project
│   ├── settings.py        # Django settings
│   ├── urls.py           # URL configuration
│   ├── core/             # Core application
│   └── users/            # Custom user model
├── manage.py             # Django management script
├── pyproject.toml        # Python dependencies
└── .github/              # CI/CD workflows
```

## Development Guidelines

### When Adding New Features
1. Update `cookiecutter.json` with new configuration options
2. Add conditional template files in `{{cookiecutter.project_slug}}/`
3. Create tests in `tests/` to validate the new feature
4. Update the README.md with feature documentation

### Testing Approach
- Use `pytest-cookies` for testing template generation
- Each configurable feature should have dedicated tests
- Test both inclusion and exclusion of optional features
- Tests are located in `tests/test_*.py` files

### Code Style
- Follow Black formatting for Python code in templates
- Use Ruff for linting Python code
- Template files should maintain consistent indentation
- Conditional blocks should be clearly commented

## Common Patterns

### Conditional File Inclusion
```jinja2
{% if cookiecutter.use_feature %}
# Feature-specific code here
{% endif %}
```

### File Naming with Variables
```
{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/settings.py
```

### Environment Variable Patterns
```python
# Using python-decouple for configuration
from decouple import config
DEBUG = config('DEBUG', default=False, cast=bool)
```

### Testing Template Generation
```python
def test_feature(cookies):
    result = cookies.bake(extra_context={'feature': 'value'})
    assert result.exit_code == 0
    # Validate generated files
```

## Maintenance Notes

### Dependencies
- Optional dependencies are included based on configuration

### Documentation
- Main documentation is in `README.md`
- Feature-specific documentation should be included in generated project README
- Keep the features list in README.md synchronized with `cookiecutter.json`

## Testing Commands

```bash
# Install dependencies
poetry install --no-root

# Run all tests
poetry run pytest tests/ -v

# Test specific feature
poetry run pytest tests/test_feature.py -v

# Generate a project locally for testing (using cruft - recommended)
cruft create . --no-input

# Generate a project locally for testing (using cookiecutter)
cookiecutter . --no-input
```

This template follows Django best practices and conventions while providing flexibility for different project requirements.
