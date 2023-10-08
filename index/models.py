from django.db import models

# Create your models here.


class message(models.Model):
    visitmessage = models.TextField(default="""
                                    # Hi,This is a placeholder, it pastors/developers, change it at /admin. 
                                    
                                    If you're a regular user and you see this message please report it to pastors/developers urgently!
                                    """)
    ourvision = models.TextField(default="""
                                    # Hi,This is a placeholder, it pastors/developers, change it at /admin. 
                                    
                                    If you're a regular user and you see this message please report it to pastors/developers urgently!
                                    """)

class system_metadata(models.Model):
    database_healthy = models.BooleanField(default=True)
    sermon_updator_on = models.BooleanField(default=False)

class pastor_email(models.Model):
    email = models.CharField(max_length=1000)

class contact_request(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    message = models.TextField()

    def __str__(self):
        name = "name: " + str(self.name) + ", email: " + str(self.email) + ", id: " + str(self.id)
        return name