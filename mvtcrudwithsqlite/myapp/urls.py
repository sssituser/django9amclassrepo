from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='signup'),
    path('edit/',views.edit,name='modify'),
    path('find/',views.find,name='search'),
    path('employees/',views.getemployees,name='emps'),
]
