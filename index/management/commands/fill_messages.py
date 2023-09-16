from django.core.management.base import BaseCommand, CommandError
from index.models import message


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        #If you want random values, check out the Faker module
        messageblock = message.objects.create(
            visitmessage="# hi",
            ourvision="#hi",
            id = 1
        )
        messageblock.save()
        print('created messages')