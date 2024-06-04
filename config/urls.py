"""
URL configuration for config project.
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


# parameters for inclusion at redoc
schema_view = get_schema_view(
    openapi.Info(
        title="Apartment API",
        default_version="v1",
        description="API endpoint for Apartment API course",
        contact=openapi.Contact(email="marcelogalli@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema_swagger"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema_redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("core_apps.users.urls")),
]


admin.site.site_header = "Roots Apartment Admin"
admin.site.site_title = "Roots Apartment Admin Portal"
admin.site.index_title = "Welcome to Roots Apartment Admin Portal"
