from django.urls import path,include
from myapp import views
urlpatterns=[
    path('',views.home),
    path('java/',views.javaexam),
    path('python/',views.pythonexam),
    path('ui/',views.uiexam),
    path('register/',views.register),
    path('accounts/',include('django.contrib.auth.urls')),
]