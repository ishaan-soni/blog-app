from django.db import models
from django.forms import widgets

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(max_length=250)





