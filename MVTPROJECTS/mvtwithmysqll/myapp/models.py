from django.db import models

# Create your models here.
class Student(models.Model):
    StuId = models.IntegerField(primary_key=True)
    StuName = models.CharField(max_length=40)
    StuMarks = models.IntegerField()
    StuImg = models.CharField(max_length=200)
