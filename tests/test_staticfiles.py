from textwrap import dedent

DEFAULT_PROJECT = "api"


def test_default_true(cookies):
    result = cookies.bake()

    assert (result.project / DEFAULT_PROJECT / "static").exists()
    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "django.contrib.staticfiles" in content
        assert "whitenoise.middleware.WhiteNoiseMiddleware" in content
        assert (
            dedent(
                """\
                # Static
                STATICFILES_DIRS = [
                    BASE_DIR / "api" / "static",
                ]
                STATIC_ROOT = BASE_DIR / "staticfiles"
                STATIC_URL = "/static/"

                STORAGES = {
                    "staticfiles": {
                        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
                    },
                }"""
            )
            in content
        )

    with open(result.project / "pyproject.toml") as f:
        assert 'whitenoise = {extras = ["brotli"], version = "' in f.read()


def test_false(cookies):
    result = cookies.bake(extra_context={"staticfiles": False})

    assert not (result.project / DEFAULT_PROJECT / "static").exists()

    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "staticfiles" not in content
        assert "whitenoise" not in content
        assert "STATIC_ROOT" not in content
        assert "STATIC_URL" not in content
        assert "STORAGES" not in content

    with open(result.project / "pyproject.toml") as f:
        assert "whitenoise" not in f.read()


def test_html_no_uses_whitenoise(cookies):
    """Test that when html is 'No', WhiteNoise storage is used instead of ManifestStaticFilesStorage"""
    result = cookies.bake(extra_context={"html": "No"})

    assert (result.project / DEFAULT_PROJECT / "static").exists()
    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "django.contrib.staticfiles" in content
        assert "whitenoise.middleware.WhiteNoiseMiddleware" in content
        assert (
            dedent(
                """\
                # Static
                STATICFILES_DIRS = [
                    BASE_DIR / "api" / "static",
                ]
                STATIC_ROOT = BASE_DIR / "staticfiles"
                STATIC_URL = "/static/"

                STORAGES = {
                    "staticfiles": {
                        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
                    },
                }"""
            )
            in content
        )

    with open(result.project / "pyproject.toml") as f:
        assert 'whitenoise = {extras = ["brotli"], version = "' in f.read()


def test_html_htmx_uses_manifest(cookies):
    """Test that when html is 'HTMX', ManifestStaticFilesStorage is used"""
    result = cookies.bake(extra_context={"html": "HTMX"})

    assert (result.project / DEFAULT_PROJECT / "static").exists()
    with open(result.project / DEFAULT_PROJECT / "settings.py") as f:
        content = f.read()
        assert "django.contrib.staticfiles" in content
        assert "whitenoise.middleware.WhiteNoiseMiddleware" in content
        assert (
            dedent(
                """\
                # Static
                STATICFILES_DIRS = [
                    BASE_DIR / "api" / "static",
                ]
                STATIC_ROOT = BASE_DIR / "staticfiles"
                STATIC_URL = "/static/"

                STORAGES = {
                    "staticfiles": {
                        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
                    },
                }"""
            )
            in content
        )

    with open(result.project / "pyproject.toml") as f:
        assert 'whitenoise = {extras = ["brotli"], version = "' in f.read()
