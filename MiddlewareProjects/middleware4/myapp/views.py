from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse(f"<h1>Home Page : {5//3}</h1>")
