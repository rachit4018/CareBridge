"""Root URL configuration."""

from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def health(_request):
    """Liveness probe. Deliberately does not touch the database — this
    answers 'is the process up', not 'is the system healthy'."""
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health, name="health"),
]
