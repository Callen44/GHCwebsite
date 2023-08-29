import os

from django.core.management.base import BaseCommand, CommandError
from index.models import system_metatdata


class Command(BaseCommand):

    def handle(self, *args, **options):
        # setup database    
        print(os.system("/app/manage.py makemigrations"))
        print(os.system("/app/manage.py migrate"))

        # fill data if database metadata says that the database is not healthy
        
        # check if the database is actually healty
        try:
            metadata = system_metatdata.objects.get(pk=1)
            database_health = bool(metadata.database_healty)
        except:
            database_health = False
        print("debug log: database health is "+ database_health+" responding")

        if database_health == False:
            self.refil()
        
        # make a superuser
        print("making super user")
        os.environ["DJANGO_SUPERUSER_PASSWORD"]=str(12345678)
        print(os.system("python /app/manage.py createsuperuser --noinput --username root --email email@example.com"))

        # mark the new database as 
        meta = system_metatdata.objects.create(database_healthy=True, id=1)
        system_metatdata.objects.filter(pk=1).update(database_healthy=True)

    def refil(self):
        # this code needs to be callable by diffrent parts of the code
        print(os.system("/app/manage.py fill_messages"))