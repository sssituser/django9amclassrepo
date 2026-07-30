from django.shortcuts import render
from django.urls import reverse_lazy
from myapp.models import Employee
from django.views.generic import *
# Create your views here.

class RegisterEmployee(CreateView):
    model = Employee
    fields = '__all__'
    
class ModifyEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    
class FindEmployee(DetailView):
    model = Employee
    fields = '__all__'

class EmployeeList(ListView):
    model = Employee
    fields = '__all__'
    
class RemoveEmployee(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees')