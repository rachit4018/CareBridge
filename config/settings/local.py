"""Local development settings.

Convenience over strictness. Never used in a deployed environment.
"""

from .base import *  # noqa: F403
from .base import env

DEBUG = True

# Fine to default here because this file is never used in production.
SECRET_KEY = env("SECRET_KEY", "dev-only-not-a-real-secret")

ALLOWED_HOSTS = ["*"]

# Show SQL in the console when you need it — flip LOG_LEVEL=DEBUG.
LOGGING["loggers"] = {  # noqa: F405
    "django.db.backends": {
        "handlers": ["console"],
        "level": env("SQL_LOG_LEVEL", "WARNING"),
        "propagate": False,
    },
}
