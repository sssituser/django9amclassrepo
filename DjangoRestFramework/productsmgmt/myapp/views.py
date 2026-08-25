from django.shortcuts import render
from myapp.Serializers import ProductSerializer
from myapp.models import Product
from rest_framework import viewsets
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    
