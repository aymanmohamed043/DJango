from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gpa = models.DecimalField(max_length=10, max_digits=2)
    image = models.ImageField(upload_to='images/', null=True)
    date_of_birth = models.DateField(null=True)
    def __str__(self):
        return self.name