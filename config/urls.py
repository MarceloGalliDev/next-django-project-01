"""
URL configuration for config project.
"""
from django.contrib import admin
from django.config import settings
from django.urls import path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]
