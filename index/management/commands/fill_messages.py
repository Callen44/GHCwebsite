from django.core.management.base import BaseCommand, CommandError
from index.models import message


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        messageblock = message.objects.create(
            visitmessage="""
# Hi, This is a placeholder, it pastors/developers, change it at /admin. 

If you're a regular user and you see this message please report it to pastors/developers urgently!
""",
            ourvision="""
# Hi, This is a placeholder, it pastors/developers, change it at /admin. 

If you're a regular user and you see this message please report it to pastors/developers urgently!
""",
            id = 1
        )
        messageblock.save()
        print('created messages')