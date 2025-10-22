from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/update/<int:code>/', views.update_course, name='update_course'),
    path('courses/delete/<int:code>/', views.delete_course, name='delete_course'),
]