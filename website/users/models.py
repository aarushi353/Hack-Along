from django.db import models
from django.contrib.auth.models import User

class Hacker(models.Model):
    name = models.CharField(max_length=100,default="abc")
    college = models.CharField(max_length=100,default="TIET")
    skill_1 = models.CharField(max_length=100,default="HTML")
    skill_2 = models.CharField(max_length=100,default="CSS")
    skill_3 = models.CharField(max_length=100,default="Js")
    
    def __str__(self):
        return self.name