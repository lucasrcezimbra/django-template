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
                    STATICFILES_DIRS = [
                        BASE_DIR / "api" / "static",
                    ]
                    STATIC_ROOT = BASE_DIR / "staticfiles"
                    STATIC_URL = "/static/"
                    STORAGES = {
                        "staticfiles": {
                            "BACKEND": config(
                                "STORAGE_STATIC_BACKEND",
                                default="whitenoise.storage.CompressedManifestStaticFilesStorage",
                            ),
                        },
                    }"""
            )
            in content
        )

    with open(result.project / "pyproject.toml") as f:
        assert 'whitenoise = {extras = ["brotli"], version = "' in f.read()

    with open(result.project / ".env") as f:
        assert (
            "STORAGE_STATIC_BACKEND=django.contrib.staticfiles.storage.StaticFilesStorage"
            in f.read()
        )

    with open(result.project / "contrib" / "env-sample") as f:
        assert (
            "STORAGE_STATIC_BACKEND=django.contrib.staticfiles.storage.StaticFilesStorage"
            in f.read()
        )


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

    # Check that STORAGE_STATIC_BACKEND is not in environment files when staticfiles is disabled
    with open(result.project / ".env") as f:
        assert "STORAGE_STATIC_BACKEND" not in f.read()

    with open(result.project / "contrib" / "env-sample") as f:
        assert "STORAGE_STATIC_BACKEND" not in f.read()
