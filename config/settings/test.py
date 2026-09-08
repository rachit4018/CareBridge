"""Test settings.

Fast and deterministic: weak password hashing, no migrations to replay.
"""

from .local import *  # noqa: F403

# MD5 is ~100x faster than PBKDF2 and these hashes never leave the test db.
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Keep tests honest about tz-aware datetimes.
USE_TZ = True
