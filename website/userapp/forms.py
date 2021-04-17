from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    skill = forms.CharField(max_length=100)
    skills = forms.CharField(max_length=100)
    linkedin = forms.CharField(max_length=100)
    github = forms.CharField(max_length=100)
    achievements = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'skills', 'linkedin', 'github', 'achievements']