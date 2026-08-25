from django.db import models

# Create your models here.
class Student(models.Model):
    StudentId = models.IntegerField(primary_key=True)
    StudentName = models.CharField(max_length=50)
    StudentMarks =models.IntegerField()