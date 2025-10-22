from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:id>', product_detail, name='product-detail'),
]
