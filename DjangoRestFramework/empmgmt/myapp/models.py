from django.db import models

# Create your models here.
class Employoee(models.Model):
    EmpId = models.IntegerField(primary_key=True)
    EmpName = models.CharField(max_length=50)
    EmpSal = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.EmpName
    
