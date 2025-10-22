from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('students/', views.students_list, name='students_list'),
    path('create/', views.create_student, name='create_student'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]

