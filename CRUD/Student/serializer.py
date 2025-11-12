from .models import Students
from rest_framework.serializers import ModelSerializer

class StudentModelSerializer(ModelSerializer):
    
    class Meta:
        model = Students
        fields = ['name','age', 'gpa']

