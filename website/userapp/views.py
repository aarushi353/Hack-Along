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

