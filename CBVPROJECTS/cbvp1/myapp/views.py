from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from myapp.models import Employee
# Create your views here.
class CreateEmployee(CreateView):
    model = Employee
    fields ='__all__'
    
class EmployeeList(ListView):
    model = Employee
    fields = '__all__'
    
class EditView(UpdateView):
    model = Employee
    fields ='__all__'
    
class FindView(DetailView):
    model = Employee
    fields ='__all__'
    
class RemoveView(DeleteView):
    model = Employee
    success_url = reverse_lazy('/')    
