"""Shared pytest fixtures.

Fixtures live here so tests read as intent rather than setup.
"""

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user(db):
    """An ordinary active user."""
    return User.objects.create_user(
        email="patient@example.com",
        password="not-a-real-password",
        first_name="Meera",
        last_name="Shah",
    )


@pytest.fixture
def superuser(db):
    return User.objects.create_superuser(
        email="admin@example.com",
        password="not-a-real-password",
    )


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
