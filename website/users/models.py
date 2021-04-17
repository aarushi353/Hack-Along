from django.db import models
from django.contrib.auth.models import User

class Hacker(models.Model):
        name = models.CharField(max_length=100),
        college = models.CharField(max_length=100),
        skill_1 = models.CharField(max_length=100),
        skill_2 = models.CharField(max_length=100),
        skill_3 = models.CharField(max_length=100),
        