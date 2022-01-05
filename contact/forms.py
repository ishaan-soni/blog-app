from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'message'
        )
    
    
