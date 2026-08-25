from django.shortcuts import render,redirect,get_object_or_404
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


def find(request,id):
    employee = get_object_or_404 (Employee,EmpId=id)
    return render(request,'myapp/find.html',{'emp':employee})
    


def edit(request,id):
    Emply = Employee.objects.get(pk=id)
    EmplyForm = EmployeeForm(instance=Emply)
    if request.method=='POST':
        EmplyForm = EmployeeForm(request.POST,instance=Emply)
        EmplyForm.save()
        return redirect("/employees")
    return render(request,'myapp/edit.html',{'Form':EmplyForm})

def delemployee(request,id):
    Emply = get_object_or_404(Employee,EmpId=id)
    if request.method == 'POST':
        Emply.delete()
        return redirect('/employees')
    return render(request,'myapp/delete.html')

def getemployees(request):
    Employees = Employee.objects.all()
    return render(request,'myapp/employees.html',{'EmpList':Employees})