from uuid import uuid4
from django.db import models

# Create your models here.


class Folder(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=64, unique=True)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    piority = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    folder = models.ForeignKey(
        Folder, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=512)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128, blank=True)
    notes = models.TextField(max_length=512, blank=True)
    star = models.BooleanField(default=False)
    piority = models.IntegerField(default=0, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
