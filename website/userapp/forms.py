from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    skills = forms.CharField(max_length=100)
    linkedin = forms.CharField(max_length=100)
    github = forms.CharField(max_length=100)
    achievements = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)

    class Meta:
        model = User
        help_texts = {
        'username': None
        }
        fields = ['username', 'email', 'password1', 'password2', 'skills', 'linkedin', 'github', 'achievements']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    skills = forms.CharField(max_length=100)
    linkedin = forms.CharField(max_length=100)
    github = forms.CharField(max_length=100)
    achievements = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)

    class Meta:
        model = User
        help_texts = {
        'username': None
        }
        fields = ['username', 'email', 'password1', 'password2', 'skills', 'linkedin', 'github', 'achievements']
            
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        