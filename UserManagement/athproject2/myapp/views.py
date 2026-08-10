from django.shortcuts import render,redirect
from myapp.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

@login_required
def javaex(request):
    return render(request,'myapp/javaexam.html')

@login_required
def pythonex(request):
    return render(request,'myapp/pythonexam.html')
@login_required
def uiex(request):
    return render(request,'myapp/uiexam.html')

def logoutview(request):
    logout(request)
    return render(request,'myapp/home.html')

def register(request):
    form = RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect('login')
    return render(request,'myapp/register.html',{'form':form})