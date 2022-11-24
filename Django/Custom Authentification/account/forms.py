from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields= ('email','nombre')

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('email','nombre')
