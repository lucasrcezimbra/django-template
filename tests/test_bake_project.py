import importlib
import os
import shlex
import subprocess
from contextlib import contextmanager

import pytest
from click.testing import CliRunner
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "pyproject.toml" in found_toplevel_files
        assert "api" in found_toplevel_files


def test_sentry_default_true(cookies):
    with bake_in_temp_dir(cookies) as result:
        with open(result.project / "api" / "settings.py") as f:
            content = f.read()
            assert "import sentry_sdk" in content
            assert 'SENTRY_DSN = config("SENTRY_DSN", default=None)' in content

        with open(result.project / "contrib" / "env-sample") as f:
            assert "SENTRY_DSN=" in f.read()

        with open(result.project / ".env") as f:
            assert "SENTRY_DSN=" in f.read()

        with open(result.project / "pyproject.toml") as f:
            assert 'sentry-sdk = {extras = ["django"], version = "' in f.read()


def test_sentry_false(cookies):
    with bake_in_temp_dir(cookies, extra_context={'use_sentry': False}) as result:
        with open(result.project / "api" / "settings.py") as f:
            content = f.read()
            assert "import sentry_sdk" not in content
            assert 'SENTRY_DSN = config("SENTRY_DSN", default=None)' not in content

        with open(result.project / "contrib" / "env-sample") as f:
            assert "SENTRY_DSN=" not in f.read()

        with open(result.project / ".env") as f:
            assert "SENTRY_DSN=" not in f.read()

        with open(result.project / "pyproject.toml") as f:
            assert 'sentry-sdk = {extras = ["django"], version = "' not in f.read()
