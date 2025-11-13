from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.core.cache import cache
# Create your views here.
from django.views.decorators.cache import cache_page
from django.db.models import Q, F


def hello(request):

    queryset = cache.get("queryset")
    if not queryset : 
    # queryset = Order.objects.all() # it will make 194 SQL queries
        queryset = Order.objects.select_related("customer").values() # it will make 1 SQL query
        cache.set("queryset", queryset, 60)
    # lab 3
    # 1. Define the search parts
    discontinued_or_expensive = Q(discontinued=1) | Q(unit_price__gt=50.0)
    not_beverages = ~Q(category__name='Beverages')

    # 2. Combine them using the AND operator 
    complex_query = Product.objects.filter(discontinued_or_expensive & not_beverages)

    # Print the results
    # print(complex_query.values('product_name', 'unit_price', 'discontinued'))
    # 2. Use the F() expression to update the value in a single, efficient SQL statement
    products_updated = Product.objects.filter(category__name='Dairy Products').update(
        unit_price=F('unit_price') * 1.10
    )

    # products_updated will hold the number of rows updated.
    # print(f"Number of products updated: {products_updated}")

    # 3. Use the F() expression to update the value in a single, efficient SQL statement
    products_updated = Product.objects.filter(category__name='Dairy Products').update(
        unit_price=F('unit_price') * 1.10
    )

    # products_updated will hold the number of rows updated.
    # print(f"Number of products updated: {products_updated}")

    # 4 
    employees_deferred = Employee.objects.defer('country')

    for emp in employees_deferred:
        print(f"Name: {emp.employee_name}, City: {emp.city}")


    # 5 
    orders_dict = Order.objects.values('id', 'order_date', 'freight', 'customer__company_name')

    for order in orders_dict:
        print(f"Order ID: {order['id']}, Order Date: {order['order_date']}, Freight: {order['freight']}, Company Name: {order['customer__company_name']}")
    
    
    # 6
    products_tuple = Product.objects.values_list('product_name', 'unit_price')

    for product in products_tuple:
        print(f"Product Name: {product[0]}, Unit Price: {product[1]}")
    
    context = {
        "queryset": list(queryset)
    }
    return render(request, "sales/sales.html", context)