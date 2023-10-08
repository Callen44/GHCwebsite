from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.message)
admin.site.register(models.system_metadata)
admin.site.register(models.pastor_email)
admin.site.register(models.contact_requests)