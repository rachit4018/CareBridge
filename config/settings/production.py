"""Production settings.

TODO (CB-4): this is intentionally incomplete. See the ticket.

Requirements:
  - DEBUG must be False, non-negotiably.
  - SECRET_KEY must come from the environment and must fail loudly if absent
    (use env(..., required=True)).
  - ALLOWED_HOSTS from the environment, never "*".
  - Security headers appropriate to a service handling health data:
    SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE,
    SECURE_HSTS_SECONDS, SECURE_PROXY_SSL_HEADER if behind a load balancer.
  - DRF should not expose the browsable API renderer.

`python manage.py check --deploy --settings=config.settings.production`
must pass with no warnings.
"""

from .base import *  # noqa: F403
