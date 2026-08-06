from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import *
def home(request):
    return render(request,'myapp/home.html')

@login_required
def javaexam(request):
    return render(request,'myapp/javaexam.html')
@login_required
def pythonexam(request):
    return render(request,'myapp/pythonexam.html')

def uiexam(request):
    return render(request,'myapp/uiexam.html')

from myapp.forms import SingUpForm
from django.http import HttpResponse
def register(request):
    form = SingUpForm()
    if request.method == "POST":
        form = SingUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        return HttpResponse('accounts/login')
    return render(request,'myapp/register.html',{'form':form})
