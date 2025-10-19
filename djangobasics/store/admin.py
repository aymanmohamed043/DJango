from django.contrib import admin
from .models import *
# Register your models here.
# store app models
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Promotion)
