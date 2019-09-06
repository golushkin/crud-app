from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(
        unique=True,
        blank= False,
        max_length=200,
        error_messages={
            "unique":"User with this email already exist",
        }
    )

    def __str__(self):
        return self.username
