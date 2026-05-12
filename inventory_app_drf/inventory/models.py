from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category =models.ForeignKey(
        Category, related_name='products', on_delete=models.PROTECT
        )
    supplier =models.ForeignKey(
        Supplier, related_name='products', on_delete=models.PROTECT
        )
    
    def __str__(self):
        return f'{self.name} ({self.sku})'
    
class StockMovement(models.Model):
    IN = 'IN'
    OUT = 'OUT'
    MOVEMENT_TYPES = [
        (IN, 'Stock In'),
        (OUT, 'Stock Out'),
    ]

    product = models.ForeignKey(
        Product, related_name='stock_movements', on_delete=models.CASCADE
    )
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movement_type} {self.quantity} of {self.product}'
