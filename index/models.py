from django.db import models

# Create your models here.


class message(models.Model):
    visitmessage = models.TextField(default="# hi")
    ourvision = models.TextField(default="# hi")

class system_metatdata(models.Model):
    database_healthy = models.BooleanField(default=True)
    sermon_updator_on = models.BooleanField(default=False)