from rest_framework import serializers
from decimal import Decimal
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # get_unit_price_with_tax = serializers.SerializerMethodField(method_name='get_unit_price_with_tax')
    collection = serializers.StringRelatedField()

def get_unit_price_with_tax(self, product: Product) -> Decimal:
    return product.unit_price * Decimal(1.1)