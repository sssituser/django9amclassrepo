from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from myapp.models import UserModel
# Create your views here.

class CreateUser(CreateView):
    model = UserModel
    fields ='__all__'
    
class UpdateUser(UpdateView):
    model = UserModel
    fields ='__all__'
    
class FindUser(DetailView):
    model = UserModel
    fields ='__all__'
    
class UserList(ListView):
    model = UserModel
    fields ='__all__'
    
class DeleteUser(DeleteView):
    model = UserModel
    success_url = reverse_lazy("users")

