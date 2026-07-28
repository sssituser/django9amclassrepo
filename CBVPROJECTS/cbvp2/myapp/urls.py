from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.StudentsList.as_view(),name="students"),
    
    path('create/',views.CreateStudent.as_view()),
    
    path('<int:pk>/',views.StudentDetails.as_view()),
    
    path('edit/<int:pk>/',views.UpdateStudent.as_view()),
    
    path('delete/<int:pk>/',views.DeleteStudent.as_view()), 
    
    
]