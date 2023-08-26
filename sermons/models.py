from django.db import models

# Create your models here.
class apikey(models.Model):
    key = models.CharField(default="")

class video(models.Model):
    official_name=models.CharField(max_length=200)
    date = models.DateField()
    vid = models.CharField()
    thumbnail_url = models.CharField(max_length=1000)
    biblestudy = models.BooleanField()