from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    def get_unit_price_with_tax(self, product: Product) -> Decimal:
        return product.unit_price * Decimal(1.1)
    
    unit_price_with_tax = serializers.SerializerMethodField(method_name='get_unit_price_with_tax')


    class Meta:
        model = Product
        # fields = ['id', 'title','description', 'unit_price', 'unit_price_with_tax', 'collection']
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']