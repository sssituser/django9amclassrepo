from django.urls import path
from myapp import views


urlpatterns=[
    path('',views.home),
    path('register/',views.register),
    path('about/',views.about),
    path('contact/',views.contact),
    path('find/<int:id>/',views.findproduct),
    path('edit/<int:id>/',views.editproduct),
    path('del/<int:id>/',views.deleteproduct),
    path('products/',views.getproducts),
]