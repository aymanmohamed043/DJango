from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductAPIViewDetails.as_view(), name='product-detail'),
]
