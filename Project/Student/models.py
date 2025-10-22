from django.db import models
from Course.models import Courses

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    date_of_birth = models.DateField()
    courses = models.ManyToManyField(Courses, related_name='students')

    def __str__(self):
        return self.name