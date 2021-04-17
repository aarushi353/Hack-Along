from django.shortcuts import render, redirect

hacker = [
    {
        'name': 'Ishaan',
        'age': '19',
        'college': 'Thapar University',
        'skill_1': 'HTML',
        'skill_2': 'CSS',
        'skill_3': 'JS',
    },
    {
        'name': 'Aarushi',
        'age': '19',
        'college': 'Thapar University',
        'skill_1': 'Django',
        'skill_2': 'UI/UX',
        'skill_3': 'Bootstrap',
    }
]

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
        'hacker' : hacker
    }
    return render(request, 'hackers.html', context)


def chat(request):
    return render(request, 'chat.html')
