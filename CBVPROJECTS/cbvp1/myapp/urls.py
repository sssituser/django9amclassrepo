from django.urls import path
from myapp import views
urlpatterns =[
    path('',views.EmployeeList.as_view(),name="employees"),
    path('create/',views.CreateEmployee.as_view()),
    path('<int:pk>/',views.FindView.as_view()),
    path('edit/<int:pk>/',views.EditView.as_view()),
    path('delete/<int:pk>/',views.RemoveView.as_view()),
]