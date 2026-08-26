from django.urls import path,include
from myapp.models import Employee
from myapp.views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',EmployeeViewSet)
urlpatterns =[
    path('',include(router.urls)),
]


