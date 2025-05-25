#!/usr/bin/env python3
"""
Script to sync dependencies between the root pyproject.toml and the template pyproject.toml.
This script reads the dependencies from the template group in the root pyproject.toml
and updates the corresponding dependencies in the template pyproject.toml.
"""

import re
import tomlkit


def read_toml_file(file_path):
    """Read a TOML file and return its content as a dictionary."""
    with open(file_path, 'r') as f:
        return tomlkit.parse(f.read())


def update_template_pyproject():
    """Update the template pyproject.toml with dependencies from the root pyproject.toml."""
    # Read the root pyproject.toml
    root_pyproject = read_toml_file("pyproject.toml")
    
    # Read the template pyproject.toml as text to preserve templating
    with open("{{cookiecutter.project_slug}}/pyproject.toml", 'r') as f:
        template_content = f.read()
    
    # Extract dependencies from the root pyproject.toml template group
    template_deps = root_pyproject.get("tool", {}).get("poetry", {}).get("group", {}).get("template", {}).get("dependencies", {})
    template_dev_deps = root_pyproject.get("tool", {}).get("poetry", {}).get("group", {}).get("template-dev", {}).get("dependencies", {})
    
    # Update regular dependencies in template pyproject.toml
    for package, version in template_deps.items():
        # Skip packages that are conditionally included (those with cookiecutter variables)
        if package in ["django-htmx", "django-ninja", "django-ninja-crud", "psycopg", "sentry-sdk", "whitenoise"]:
            continue
        
        # For regular dependencies, update the version
        if isinstance(version, dict) and "extras" in version:
            # Handle dependencies with extras
            version_str = f"{{extras = {version['extras']!r}, version = \"{version['version']}\"}}"
            pattern = rf'{package}\s*=\s*{{[^}}]*}}'
            template_content = re.sub(pattern, f"{package} = {version_str}", template_content)
        else:
            # Handle regular dependencies
            version_str = str(version)
            pattern = rf'{package}\s*=\s*"[^"]+"'
            template_content = re.sub(pattern, f'{package} = "{version_str}"', template_content)
    
    # Update dev dependencies in template pyproject.toml
    for package, version in template_dev_deps.items():
        pattern = rf'{package}\s*=\s*"[^"]+"'
        template_content = re.sub(pattern, f'{package} = "{version}"', template_content)
    
    # Write back the updated template pyproject.toml
    with open("{{cookiecutter.project_slug}}/pyproject.toml", 'w') as f:
        f.write(template_content)


if __name__ == "__main__":
    update_template_pyproject()
    print("Template dependencies have been synchronized successfully!")