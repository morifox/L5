from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, RepairViewSet, SaleViewSet
from .views import home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Auto Center API",
        default_version='v1',
        description="API для управления данными автомобилей, ремонтов и продаж",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@autocenter.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'repairs', RepairViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]
