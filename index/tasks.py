# tasks for index app

from celery import shared_task

@shared_task
def email_pastors_new_message():
    # Send the pastors email notifying them of the new message
    from django.core.mail import send_mail
    print('log: sending mail to pastors')
    print('! this function dose not work !')