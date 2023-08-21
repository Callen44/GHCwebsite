from django.apps import AppConfig


class SermonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sermons'

    def ready(self):
        from datetime import datetime, timedelta
        from sermons.tasks import cel_reset_db
        from django.utils import timezone

        # schedule the resetting of the database

        # figure out how long until 12:00 on the next sunday,
        now = datetime.now()

        next_sunday = now + timedelta(days=(6 - now.weekday()))
        next_sunday = next_sunday.replace(hour=12, minute=0, second=0, microsecond=0)

        cel_reset_db.apply_async(eta=timezone.now())
