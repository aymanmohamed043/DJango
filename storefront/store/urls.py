from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductAPIViewDetails.as_view(), name='product-detail'),
    path('collections', CollectionAPIView.as_view(), name='collections_list'),
    path('collections/<int:pk>', CollectionAPIViewDetails.as_view(), name='collection_details')
]
