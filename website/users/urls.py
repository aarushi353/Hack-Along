from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('hackathons/', views.hackathons, name="hackathons"),
    path('hackers/', views.hackers, name="hackers"),
    path('chat/', views.chat, name="chat"),
    path('profile/', views.chat, name="profile"),
]
