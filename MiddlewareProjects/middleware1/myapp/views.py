from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def home(requet):
    return HttpResponse(f"<h1 style='text-align:center'>Home Page  {10//2}</h1>")
