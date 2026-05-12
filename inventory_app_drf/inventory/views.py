from rest_framework import viewsets
from .permissions import IsStaffOrReadOnly
from .models import Category, Product, StockMovement, Supplier
from .serializers import CategorySerializer, ProductSerializer, StockMovementSerializer, SupplierSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    lookup_field = 'slug'
    filterset_fields = ['name']
    ordering_fields = ['name']


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ['name']
    ordering_fields = ['name']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category', 'supplier').all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ['category', 'supplier', 'price']
    ordering_fields = ['price', 'quantity', 'name']
    search_fields = ['name', 'sku']


class StockMovementViewSet(viewsets.ModelViewSet):
    queryset = StockMovement.objects.select_related('product').all()
    serializer_class = StockMovementSerializer
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ['movement_type', 'product']
    ordering_fields = ['created_at', 'quantity']