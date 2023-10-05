import os

from django.core.management.base import BaseCommand, CommandError
from index.models import system_metatdata


class Command(BaseCommand):

    def handle(self, *args, **options):
        # setup database    
        print(os.system("/app/manage.py makemigrations index sermons"))
        print(os.system("/app/manage.py sqlmigrate index 0001"))
        print(os.system("/app/manage.py sqlmigrate sermons 0002"))
        print(os.system("/app/manage.py migrate"))

        # fill data if database metadata says that the database is not healthy
        
        # check if the database is actually healty
        try:
            metadata = system_metatdata.objects.get(pk=1)
            database_health = bool(metadata.database_healty)
        except:
            database_health = False
        print("debug log: database health is "+ str(database_health)+" responding")

        if database_health == False:
            self.refil()
        
        # prepare celery
        self.celeryman()

        # prepage static files
        self.staticprep()

        # make a superuser
        print("making super user")
        os.environ["DJANGO_SUPERUSER_PASSWORD"]=str(12345678)
        print(os.system("python /app/manage.py createsuperuser --noinput --username root --email email@example.com"))

        # mark the new database as good
        meta = system_metatdata.objects.create(database_healthy=True, id=1)
        system_metatdata.objects.filter(pk=1).update(database_healthy=True)

    def refil(self):
        # this code needs to be callable by diffrent parts of the code
        print(os.system("/app/manage.py fill_messages"))
    
    def celeryman(self):
        print('preparing celery')
        from datetime import datetime, timedelta
        from sermons.tasks import cel_reset_db
        from django.utils import timezone
        from index.models import system_metatdata
        import os

        # figure out how long until 12:00 on the next sunday, and schedule the task
        now = datetime.now()

        next_sunday = now + timedelta(days=(6 - now.weekday()))
        next_sunday = next_sunday.replace(hour=12, minute=0, second=0, microsecond=0)

        cel_reset_db.apply_async(eta=timezone.now())
        cel_reset_db.apply_async(eta=next_sunday)
    
    def staticprep(self):
        print('preparing static files')
        os.system("python /app/manage.py collectstatic --noinput -c")