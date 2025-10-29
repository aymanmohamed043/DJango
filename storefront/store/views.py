from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializer import *
# Create your views here.


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':

        queryset = Product.objects.prefetch_related('collection').all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return RecursionError(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
    
