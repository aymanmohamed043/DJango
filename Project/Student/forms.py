
from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'age', 'image', 'date_of_birth', 'courses']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
