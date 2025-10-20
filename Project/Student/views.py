from django.shortcuts import get_object_or_404, render, redirect
from Course.models import Courses
from .models import Students
from .forms import StudentForm

students = Students.objects.prefetch_related('courses').all()

# Create your views here.

def home (request): 
    return render(request, 'base.html')

def students_list(request):
    students = Students.objects.prefetch_related('courses').all()
    context = {'students': students}
    return render(request, 'student_list.html', context)

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students_list')
    return render(request, 'delete_student.html', {'student': student})