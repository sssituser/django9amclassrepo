from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Student
from myapp.forms import StudentForm

# Create your views here.
def home(request):
    students =Student.objects.all()
    return render(request,'home.html',{"StuList":students})

def register(request):
    sform = StudentForm()    
    if request.method == 'POST':
        sform = StudentForm(request.POST)
        if sform.is_valid():
            sform.save(commit=True)
            return redirect('/')
    return render(request,'register.html',{"form":sform})
def getstuent(request,id):
    student = get_object_or_404(Student,id=id)
    return render(request,'find.html',{"stu":student})




    
    
