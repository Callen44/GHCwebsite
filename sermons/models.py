from django.db import models

# Create your models here.
class apikey(models.Model):
    key = models.CharField(default="")

class video(models.Model):
    official_name=models.CharField(max_length=None)
    date = models.DateField()
    # vid_url = models.CharField(max_length=None)
    thumbnail_url = models.CharField(max_length=None)
    biblestudy = models.BooleanField()
    id = models.CharField(max_length=None, primary_key=True)