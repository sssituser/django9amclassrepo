from django.db import models

# Create your models here.
class Product(models.Model):
    ProductId = models.IntegerField(primary_key=True)
    ProductName = models.CharField(max_length=50)
    ProductPrice = models.DecimalField(max_digits=10,decimal_places=2)
    