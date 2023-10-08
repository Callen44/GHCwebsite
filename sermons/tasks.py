# Tasks for sermons app

from celery import shared_task
from .reset_db_file import reset_db
from datetime import datetime, timedelta
from django.utils import timezone
from index.models import system_metadata
import os


@shared_task
def cel_reset_db():
    reset_db()
    print('log: task complete, sermons updated, scheduling for next sunday')

    # Personal note, I know this should not be commited to the repo
    print('!!!! there needs to be a multi week run of the server to properly test this !!!')

    # Schedule the task to run again on next sunday

    # figure out how long until 12:00 on the next sunday, and schedule the task
    now = datetime.now()
    next_sunday = now + timedelta(days=(6 - now.weekday()))
    next_sunday = next_sunday.replace(hour=12, minute=0, second=0, microsecond=0)
    # Run the task on the next sunday
    cel_reset_db.apply_async(eta=next_sunday)