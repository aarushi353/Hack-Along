from django.shortcuts import render,redirect


def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def hackathons(request):
    return render(request, 'hackathons.html')

def register(request):
    return render(request, 'Register.html')

