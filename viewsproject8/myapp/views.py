from django.shortcuts import render

# Create your views here.
def home(request):
    dict = { "ID":112, "Name":"Raj", "Age" : 20,"Edu" : "Graduation",
            "Marks":500
    }
    return render(request,'myapp/home.html',dict)
