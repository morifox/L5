from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.shortcuts import redirect
schema_view = get_schema_view(
    openapi.Info(
        title="Auto Center API",
        default_version='v1',
        description="API for managing car sales and repairs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@autocenter.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Разрешение для всех пользователей
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('', lambda request: redirect('swagger-schema', permanent=False)),  # Редирект на Swagger
    path('accounts/', include('django.contrib.auth.urls')),  # Подключение стандартных URL аутентификации
]
