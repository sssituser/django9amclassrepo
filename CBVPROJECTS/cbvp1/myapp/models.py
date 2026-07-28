from django.db import models
from django.urls import reverse
# Create your models here.
class Employee(models.Model):
    EmpId = models.IntegerField(primary_key=True)
    EmpName = models.CharField(max_length=50)
    EmpSal = models.DecimalField(max_digits=8,decimal_places=2)
    def get_absolute_url(self):
        return reverse('employees')
    