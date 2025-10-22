from django.contrib import admin
from .models import Students
# Register your models here.

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'date_of_birth' , 'get_courses')
    filter_horizontal = ('courses',) 

    def get_courses(self, obj):
        return ", ".join([course.name for course in obj.courses.all()])
