from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="User Authentication API",
        default_version="v1",
        description="API documentation for the Custom User Authentication System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your@email.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/user/", include("user.urls")),

    # Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-ui",
    ),

    # Redoc
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="redoc",
    ),

    # Raw schema
    path(
        "swagger.json",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]