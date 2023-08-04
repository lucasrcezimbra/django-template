#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path().absolute()


if __name__ == "__main__":
    if not {{cookiecutter.use_heroku}}:
        (PROJECT_DIRECTORY / "Procfile").unlink()
