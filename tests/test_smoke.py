"""Smoke tests.

These prove the wiring works. If these fail, nothing else is worth debugging.
"""

import pytest
from django.urls import reverse


def test_health_endpoint_returns_ok(client):
    response = client.get(reverse("health"))
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.django_db
def test_settings_use_custom_user_model():
    from django.contrib.auth import get_user_model

    assert get_user_model()._meta.label == "users.User"
