from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms

 
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Personal_data  # Ensure this import if it's in another file



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]