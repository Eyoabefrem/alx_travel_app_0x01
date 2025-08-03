#!/usr/bin/env python3
"""
URL configuration for alx_travel_app project.

Includes routes for Swagger API documentation.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ALX Travel API",
      default_version='v1',
      description="API documentation for ALX Travel Project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@alxtravel.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),  # Assume listings has urls.py for API endpoints

    # Swagger endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0, renderer='yaml'), name='schema-yaml'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('listings.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
