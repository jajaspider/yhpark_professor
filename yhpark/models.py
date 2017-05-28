from django.db import models

# Create your models here.

class  Professor(models.Model):
    author = models.ForeignKey('auth.User')
    force = models.CharField()
    research = models.CharField()
    academy = models.CharField()
    awards = models.CharField()
    student = models.CharField()
