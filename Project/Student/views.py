from django.shortcuts import render

# Create your views here.

def home (request): 
    return render(request, 'base.html')

def students_list(request):
    return render(request, 'students_list.html')