from django.shortcuts import render, redirect, get_object_or_404
from .models import Courses

def courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'courses_list.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')

        if code and name:
            Courses.objects.create(code=code, name=name)
            return redirect('courses_list')
    return render(request, 'create_course.html')

def update_course(request, code):
    course = get_object_or_404(Courses, code=code)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.save()
        return redirect('courses_list')
    return render(request, 'update_course.html', {'course': course})

def delete_course(request, code):
    course = get_object_or_404(Courses, code=code)
    if request.method == 'POST':
        course.delete()
        return redirect('courses_list')
    return render(request, 'delete_course.html', {'course': course})
