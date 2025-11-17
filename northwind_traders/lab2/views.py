from django.shortcuts import render
from django.db.models import Sum
from sales.models import *
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.db.models import Count
from django.http import JsonResponse
from .tasks import generate_monthly_sales_report, send_invoices_to_all_customers


# Create your views here.
# lab 2
# 1. Create a function that returns the top 10 selling products
def get_top_selling_products():
    cache_key = "top_10_products"

    data = cache.get(cache_key)
    if data is not None:
        return data  

    # heavy  aggregation
    data = (
        OrderDetails.objects
        .values('product__product_name')
        .annotate(total_qty=Sum('quantity'))
        .order_by('-total_qty')[:10]
    )

    cache.set(cache_key, data, timeout=60 * 5)  
    return data


# 2. Create a function that returns the top 10 customers with the most orders
def get_customers_with_order_count():
    key = "customers_order_count"

    if cached := cache.get(key):
        return cached

    qs = (
        Customer.objects
        .annotate(order_count=Count('order'))
        .order_by('-order_count')
    )

    cache.set(key, list(qs), 60 * 10)  # 10 minutes
    return qs



# 3. Create a function that returns the sales report
@cache_page(60 * 2)  # 2 minutes cache
def sales_report(request):
    sales = (
        Order.objects
        .values('order_date__month')
        .annotate(total=Sum('orderdetail__unit_price'))
    )
    return render(request, "reports/sales.html", {"sales": sales})

###########################################

# LAB Celery, Redis as Msg Broker, Flower)
def run_heavy_report(request):
    task = generate_monthly_sales_report.delay()   # run in background
    return JsonResponse({"task_id": task.id})

def send_invoices(request):
    task = send_invoices_to_all_customers.delay()
    return JsonResponse({"task_id": task.id})
