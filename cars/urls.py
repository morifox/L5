from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, RepairViewSet, SaleViewSet
from .views import home

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'repairs', RepairViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    
]
