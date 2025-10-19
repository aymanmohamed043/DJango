from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import Q, F
from .models import *


# Create your views here.
def index(request):
    try:
        # customers = Customer.objects.filter(email__endswith='@google.nl').values('first_name', 'last_name', 'email')
        # count = customers.count()
        querysets = Product.objects.select_related('collection').all()
        count = querysets.count()
    except Product.DoesNotExist:
        return Http404("Product does not exist")
    context = {
        # 'customers': customers,
        'querysets': querysets,
        'count': count
    }
    return render(request, 'store/store.html', context)
