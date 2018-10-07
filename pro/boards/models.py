from django.db import models
from django import forms


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    message = models.CharField(
        max_length=2000,
    )
