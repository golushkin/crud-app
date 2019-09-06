from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
