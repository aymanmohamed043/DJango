from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView   
from rest_framework import status
from django.db.models import Count
from .models import *
from .serializer import *
# Create your views here.


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # def get(self, request):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAPIViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=pk)

        
    # def get(self, request, pk):
    #     product = self.get_object(pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     product = self.get_object(pk)
    #     serializer = ProductSerializer(product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        product = self.get_object()
        if product.order_items.count() > 0:
            return Response({"error": f"Can't delete this product as it related to order items {product.order_items.all()}"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

###############################################3
class CollectionAPIView(APIView):
    def get(self, request):
        collections = Collection.objects.annotate(products_count=Count('products')).all()
        serializer = CollectionSerializer(collections, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CollectionAPIViewDetails(APIView):
    def get_object(self, pk):
        try:
            return Collection.objects.annotate(products_count=Count('products')).get(pk=pk)
        except:
            return Response({"error": "object not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        collection = self.get_object(pk=pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    
    def put(self, request, pk):
        collection = self.get_object(pk=pk)
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, pk):
        collection = self.get_object(pk=pk)
        if collection.products.count() > 0:
            return Response({"error": f"Can't delete this collection as it related to ({collection.products.count()}) products "}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    