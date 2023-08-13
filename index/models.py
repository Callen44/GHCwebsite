from django.db import models

# Create your models here.


class message(models.Model):
    visitmessage = models.TextField()
    ourvision = models.TextField()