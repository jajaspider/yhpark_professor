from django.db import models

# Create your models here.

class Professor(models.Model):
    author = models.CharField(max_length=7)
    force = models.TextField()
    research = models.TextField()
    academy = models.TextField()
    awards = models.TextField()
    student = models.TextField()

class Notice(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField()
    notice_url = models.URLField(max_length=200, default='http://sonagod.tk:20017')
    post_time = models.DateTimeField(auto_now=False,auto_now_add=True)
