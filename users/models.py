""" CustomUserModel for user registration and authentication """

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    """ Custom User Model """
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
