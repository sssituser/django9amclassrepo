from django.db import models
from django.urls import reverse
# Create your models here.
class Employee(models.Model):
    EmployeeId = models.IntegerField(primary_key=True)
    EmployeeName = models.CharField(max_length=40)
    EmployeeSalary = models.DecimalField(max_digits=8,decimal_places=2)
    
    
    def get_absolute_url(self):
        return reverse('employees')