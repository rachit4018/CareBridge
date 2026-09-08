#!/usr/bin/env python
"""Django management entrypoint.

Defaults to local settings so `./manage.py runserver` works without ceremony.
Deployed processes set DJANGO_SETTINGS_MODULE explicitly.
"""

import os
import sys


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Is it installed and is your virtualenv active?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
