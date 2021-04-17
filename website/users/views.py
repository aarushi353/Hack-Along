from django.shortcuts import render, redirect
from .models import Hacker


def home(request):
    return render(request, 'index.html')

def hackathons(request):
    return render(request, 'hackathons.html')


def hackers(request):
    context={ 
        'hacker': Hacker.objects.all()
    }
    return render(request, 'hackers.html', context)


def chat(request):
    return render(request, 'chat.html')

def profile(request):
    return render(request, 'chat.html')

