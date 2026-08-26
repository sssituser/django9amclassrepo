from django.shortcuts import render
from myapp.models import Employee
from myapp.Serializers import EmployeeSerializer
from rest_framework import viewsets
# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer
    