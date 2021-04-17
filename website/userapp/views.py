<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
            form = UserRegisterForm()
    return render(request, 'userapp/register.html', {'form': form})

=======
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def register(request):
    if request.method == 'HACKER':
    form = UserCreationForm(request.HACKER)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {First Name}!')
        return redirect('home')
    else:
    form = UserCreationForm()
    return render(request, 'users/templates/Register.html', {'form': form})
>>>>>>> 55372badcc0b8708ffd225ff84aa22ef8ae76018

