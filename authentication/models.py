from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=50, unique=True)
    email = models.EmailField(
        ('email address'), unique=True, primary_key=True)
    password = models.CharField(
        ('master password'), max_length=256)
    hint = models.CharField(max_length=256)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
