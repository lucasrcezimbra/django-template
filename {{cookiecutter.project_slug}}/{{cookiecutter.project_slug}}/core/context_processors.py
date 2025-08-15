{% if cookiecutter.use_sentry %}from django.conf import settings
from decouple import config


def sentry_context(request):
    """Add Sentry configuration to template context."""
    return {
        "SENTRY_DSN": getattr(settings, "SENTRY_DSN", None),
        "SENTRY_ENV": config("ENV", default="production"),
    }
{% endif %}