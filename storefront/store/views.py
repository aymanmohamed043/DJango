from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
# Create your views here.


@api_view(['GET'])
def product_list(request):
    queryset = Product.objects.prefetch_related('collection').all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)