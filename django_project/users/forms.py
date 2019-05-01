from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms import ModelForm
from .models import AccountUser




class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = AccountUser
        fields = ['first_name','last_name','username', 
        'email', 'password1', 'password2','location','phone_number']