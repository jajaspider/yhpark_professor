from django.db import models

# Create your models here.

class Professor(models.Model):
    author = models.CharField(max_length=7)
    force = models.CharField(max_length=500)
    research = models.TextField(max_length=500)
    academy = models.TextField(max_length=500)
    awards = models.CharField(TextField=500)
    student = models.CharField(TextField=500)
