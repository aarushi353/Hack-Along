from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def hackathons(request):
    return render(request, 'hackathons.html')


def register(request):
    return render(request, 'Register.html')


def hackers(request):
    return render(request, 'hackers.html')


def chat(request):
    return render(request, 'chat.html')
