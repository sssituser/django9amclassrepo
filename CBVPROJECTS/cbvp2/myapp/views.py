from django.shortcuts import render
from django.urls import reverse_lazy
from myapp.models import Student
from django.views.generic import *

# Create your views here.

class CreateStudent(CreateView):
    model = Student
    fields = '__all__'
    
class StudentsList(ListView):
    model = Student
    fields = '__all__'
    
class UpdateStudent(UpdateView):
    model = Student
    fields = '__all__'
    
class StudentDetails(DetailView):
    model = Student
    fields = '__all__'
    
class DeleteStudent(DeleteView):
    model = Student
    success_url = reverse_lazy("students")
