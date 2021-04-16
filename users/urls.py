from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('hackathons/', views.hackathons, name="hackathons"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('hackers/', views.hackers, name="hackers"),
]
