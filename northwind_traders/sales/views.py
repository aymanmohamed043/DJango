from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.core.cache import cache
# Create your views here.
from django.views.decorators.cache import cache_page


@cache_page(60)
def hello(request):

    queryset = cache.get("queryset")
    if not queryset : 
    # queryset = Order.objects.all() # it will make 194 SQL queries
        queryset = Order.objects.select_related("customer").values() # it will make 1 SQL query
        cache.set("queryset", queryset, 60)

    context = {
        "queryset": list(queryset)
    }
    return render(request, "sales/sales.html", context)