from django.shortcuts import render, redirect
from .models import Hacker


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def hackathons(request):
    return render(request, 'hackathons.html')


def register(request):
    return render(request, 'Register.html')


def hackers(request):
    context={ 
        'hacker' : Hacker.objects.all()
    }
    return render(request, 'hackers.html', context)


def chat(request):
    return render(request, 'chat.html')
