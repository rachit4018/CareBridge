"""User model tests.

TICKET CB-5 leaves one of these deliberately unwritten — see the TODO.
"""

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

pytestmark = pytest.mark.django_db


def test_create_user_normalises_email():
    user = User.objects.create_user(email="Meera@Example.COM", password="x" * 12)
    assert user.email == "meera@example.com"


def test_create_user_without_email_is_rejected():
    with pytest.raises(ValueError, match="email address"):
        User.objects.create_user(email="", password="x" * 12)


def test_superuser_has_staff_and_superuser_flags():
    admin = User.objects.create_superuser(email="a@example.com", password="x" * 12)
    assert admin.is_staff
    assert admin.is_superuser


def test_full_name_falls_back_to_email(user):
    user.first_name = ""
    user.last_name = ""
    assert user.display_name == user.email


# TODO (CB-5): add a test proving two users cannot share an email address,
# including the case where they differ only by letter case. Think about what
# exception Django raises and at which layer.