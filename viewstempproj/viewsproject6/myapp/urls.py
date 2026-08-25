from django.urls import path
from django.http import HttpResponse
from myapp import views

urlpatterns=[
    path('',views.home),
    path('reg/',views.register),
    path('login/',views.Login),
    path('about/',views.about),
    path('contact/',views.contact),
]
