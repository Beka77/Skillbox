from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(
        max_length=100, 
        null = True, blank = True, 
        default='0'
    )
    profile_image = models.ImageField(
        upload_to = 'profile_image/', 
       verbose_name = 'Изображение профиля',
       blank = True, null = True,
       default = None 
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер",
        blank = True, null = True
    )
    def __str__(self):
        return f"{self.username}"
    

class RequestForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  request = forms.CharField(widget=forms.Textarea)