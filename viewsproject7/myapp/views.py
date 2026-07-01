from django.shortcuts import render

# Create your views here.
def home(request):
    dict={"ID":111,"Name":"Kiran Kumar","Marks":4000}
    return render(request,'myapp/home.html',dict)