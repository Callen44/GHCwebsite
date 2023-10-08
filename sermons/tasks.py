# Tasks for sermons app

from celery import shared_task
from .reset_db_file import reset_db


@shared_task
def cel_reset_db():
    reset_db()
    print('log: task complete, sermons updated, scheduling for next sunday')
    