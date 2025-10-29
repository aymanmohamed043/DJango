from rest_framework import serializers
from decimal import Decimal
from .models import Product

# class ProductSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     unit_price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     unit_price_with_tax = serializers.SerializerMethodField(method_name='get_unit_price_with_tax')
#     collection = serializers.StringRelatedField()

#     def get_unit_price_with_tax(self, product: Product) -> Decimal:
#         return product.unit_price * Decimal(1.1)

class ProductSerializer(serializers.ModelSerializer):
    def get_unit_price_with_tax(self, product: Product) -> Decimal:
        return product.unit_price * Decimal(1.1)
    
    unit_price_with_tax = serializers.SerializerMethodField(method_name='get_unit_price_with_tax')


    class Meta:
        model = Product
        # fields = ['id', 'title','description', 'unit_price', 'unit_price_with_tax', 'collection']
        fields = '__all__'