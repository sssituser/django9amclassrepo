from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.EmployeeList.as_view(),name="employees"),
    path('create/',views.RegisterEmployee.as_view()),
    path('<int:pk>/',views.FindEmployee.as_view()),
    path('edit/<int:pk>/',views.ModifyEmployee.as_view()),
    path('delete/<int:pk>/',views.RemoveEmployee.as_view()),
]