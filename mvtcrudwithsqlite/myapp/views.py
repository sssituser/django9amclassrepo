from django.shortcuts import render,redirect
from myapp.forms import EmployeeForm
from myapp.models import Employee

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def register(request):
    EmpForm = EmployeeForm()
    if request.method == 'POST':
        EmpForm = EmployeeForm(request.POST)
        if EmpForm.is_valid():
            EmpForm.save(commit=True)
            return redirect('/employees')
    return render(request,'myapp/register.html',{'Form':EmpForm})


def find(request):
    return render(request,'myapp/find.html')


def edit(request):
    return render(request,'myapp/edit.html')

def getemployees(request):
    Employees = Employee.objects.all()
    return render(request,'myapp/employees.html',{'EmpList':Employees})