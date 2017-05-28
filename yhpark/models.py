from django.db import models

# Create your models here.

class Professor(models.Model):
    author = models.CharField(max_length=7)
    force = models.CharField(max_length=500)
    research = models.CharField(max_length=500)
    academy = models.CharField(max_length=500)
    awards = models.CharField(max_length=500)
    student = models.CharField(max_length=500)
