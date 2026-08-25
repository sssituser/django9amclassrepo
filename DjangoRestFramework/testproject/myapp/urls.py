from django.urls import path,include
from myapp.views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students',StudentViewSet)
urlpatterns=[
    path('',include(router.urls)),
]