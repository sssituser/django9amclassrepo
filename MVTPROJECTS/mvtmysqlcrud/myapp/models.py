from django.db import models

# Create your models here.
class Product(models.Model):
    ProId = models.IntegerField()
    ProName = models.CharField(max_length=40)
    ProImg = models.CharField(max_length=100)
    ProPrice = models.IntegerField()
