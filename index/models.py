from django.db import models

# Create your models here.


class message(models.Model):
    ourvisiontitle = models.CharField(max_length=500)
    ourvision = models.TextField()