from django.urls import path, include
from .views import (
    CategoryViewSet, SupplierViewSet,
    ProductViewSet, StockMovementViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('suppliers', SupplierViewSet)
router.register('products', ProductViewSet)
router.register('movements', StockMovementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]