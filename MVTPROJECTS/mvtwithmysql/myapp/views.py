from django.shortcuts import render
from myapp.models import Employee
# Create your views here.
def home(request):
    Employees = Employee.objects.all()
    return render(request,'home.html',{'EmpList':Employees})
    
