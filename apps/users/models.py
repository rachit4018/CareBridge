"""User model.

Two decisions worth understanding before you extend this in Sprint 1.

**Why a custom model at all, on day one?**
Django's `AUTH_USER_MODEL` can only be swapped cleanly before the first
migration. Afterwards, every table with a foreign key to `auth.User` needs
manual migration surgery. It costs nothing now and is expensive later, so it
is always done first — even when, as here, the model starts almost empty.

**Why email instead of username?**
This is a healthcare portal. Patients will be invited by email, not asked to
invent a username. Carrying an unused `username` column would mean generating
throwaway values on every invite.

Sprint 1 extends this with a role and an organization foreign key. It is
deliberately left minimal here.
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """Manager for a user model whose natural key is email, not username."""

    use_in_migrations = True

    def _create_user(self, email: str, password: str | None, **extra):
        if not email:
            raise ValueError("Users must have an email address.")
        # normalize_email lowercases only the domain part; the local part is
        # case-sensitive per RFC, but in practice nobody relies on that, so we
        # lowercase the whole thing to avoid duplicate accounts.
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str | None = None, **extra):
        extra.setdefault("is_staff", False)
        extra.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra)

    def create_superuser(self, email: str, password: str | None = None, **extra):
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)
        if extra.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra)


class User(AbstractBaseUser, PermissionsMixin):
    """A person who can sign in.

    Extends AbstractBaseUser rather than AbstractUser because AbstractUser
    brings a `username` field we do not want and cannot remove cleanly.
    """

    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80, blank=True)

    is_active = models.BooleanField(
        default=True,
        help_text="Deactivate rather than delete — audit trails must keep pointing at a real row.",
    )
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []  # prompted by createsuperuser besides email

    class Meta:
        ordering = ["email"]

    def __str__(self) -> str:
        return self.email

    @property
    def display_name(self) -> str:

        """Safe to render anywhere. Falls back to email when no name is set.
        
        TODO: revisit once invitations exist. Showing an email where a name
        belongs may disclose more than intended on shared screens.
        """
        
        return f"{self.first_name} {self.last_name}".strip() or self.email
