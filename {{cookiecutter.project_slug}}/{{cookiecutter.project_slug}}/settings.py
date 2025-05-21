from pathlib import Path

{% if cookiecutter.use_sentry -%}
import sentry_sdk
{%- endif %}
from decouple import Csv, config
from dj_database_url import parse as dburl

{% if cookiecutter.use_sentry -%}
SENTRY_DSN = config("SENTRY_DSN", default=None)
if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN, environment=config("ENV"))
{% endif -%}

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default=[], cast=Csv())


# Application definition
INSTALLED_APPS = [
    "{{ cookiecutter.project_slug }}.core",
    "{{ cookiecutter.project_slug }}.users",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    {%- if cookiecutter.staticfiles %}
    "django.contrib.staticfiles",
    {%- endif %}
    "django_extensions",
    {%- if cookiecutter.html == "HTMX" %}
    "django_htmx",
    {%- endif %}
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    {%- if cookiecutter.staticfiles %}
    "whitenoise.middleware.WhiteNoiseMiddleware",
    {%- endif %}
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    {%- if cookiecutter.html == "HTMX" %}
    "django_htmx.middleware.HtmxMiddleware",
    {%- endif %}
]

ROOT_URLCONF = "{{ cookiecutter.project_slug }}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "{{ cookiecutter.project_slug }}.wsgi.application"


# Database
default_db = config("DATABASE_URL", cast=dburl)
{% if cookiecutter.database != "SQLite" %}
# Connection pool settings for PostgreSQL
default_db["CONN_MAX_AGE"] = 60  # seconds
default_db["CONN_HEALTH_CHECKS"] = True
default_db["OPTIONS"] = {**default_db.get("OPTIONS", {}), "pool_size": 10}
{% endif %}
DATABASES = {
    "default": default_db,
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Auth
AUTH_USER_MODEL = "users.User"


{%- if cookiecutter.staticfiles %}
# Static
STATICFILES_DIRS = [
    BASE_DIR / "{{cookiecutter.project_slug}}" / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
{%- endif %}
