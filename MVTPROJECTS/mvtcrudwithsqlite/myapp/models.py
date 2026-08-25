from django.db import models

# Create your models here.

class Employee(models.Model):
    EmpId = models.IntegerField(primary_key=True)
    EmpName = models.CharField(max_length=40)
    EmpSal = models.DecimalField(max_digits=8,decimal_places=2)
