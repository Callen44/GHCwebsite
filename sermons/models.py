from django.db import models

# Create your models here.
class apikey(models.Model):
    key = models.CharField(default="")

class page(models.Model):
    pageToken = models.CharField(max_length=None)

class video(models.Model):
    official_name=models.CharField(max_length=None)
    date = models.DateField()
    vid_url = models.CharField(max_length=None)
    thumbnail_url = models.CharField(max_length=None)
    biblestudy = models.BooleanField()
    page = models.ForeignKey(page, on_delete=models.CASCADE)
    youtubeid = models.CharField(max_length=None)