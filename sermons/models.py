from django.db import models

# Create your models here.
class apikeys(models.Model):
    key = models.CharField(default="")

class video(models.Model):
    date = models.TimeField()
    vid = models.CharField()
    