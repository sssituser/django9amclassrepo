from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Employoee
from myapp.Serializers import EmployeeSerializer
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employoee.objects.all()
    serializer_class = EmployeeSerializer
