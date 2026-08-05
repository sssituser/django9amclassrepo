from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class UserModel(User):
    def get_absolute_url(self):
        return reverse("users")