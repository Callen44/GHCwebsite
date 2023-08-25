from django.db import models

# Create your models here.
class apikey(models.Model):
    key = models.CharField(default="")

class video(models.Model):
    official_name=models.CharField()
    date = models.TimeField()
    vid = models.CharField()
    thumbnail_url = models.CharField()
    