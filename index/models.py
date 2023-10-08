from django.db import models

# Create your models here.


class message(models.Model):
    visitmessage = models.TextField(default="# hi")
    ourvision = models.TextField(default="# hi")

class system_metadata(models.Model):
    database_healthy = models.BooleanField(default=True)
    sermon_updator_on = models.BooleanField(default=False)

class pastor_email(models.Model):
    email = models.CharField(max_length=1000)

class contact_requests(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    message = models.TextField()