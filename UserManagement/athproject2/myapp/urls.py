from django.urls import path,include
from myapp import views

urlpatterns =[
    path('',views.home),
    path('create/',views.register),
    path('javaex/',views.javaex),
    path('pythonex/',views.pythonex),
    path('uiex/',views.uiex),
    path('logout/',views.logoutview),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
]