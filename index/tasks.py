# tasks for index app

from celery import shared_task
from . import models
from django.core.mail import send_mail

@shared_task
def email_pastors_new_message(message_id):
    # Send the pastors email notifying them of the new message
    print('log: sending mail to pastors')

    # find the message in the database so that the pastors can read it from their email
    message = models.contact_request.objects.get(id=message_id)
    email_message = """A new Contact Us request was recieved!
    
    info:
    name: """ + str(message.name) + """
    email: """ + str(message.email)+"""
    message:
    
    """ + str(message.message)

    print (email_message)
    
    emails = models.pastor_email.objects.all()
    for email in emails:
        email = str(email.email)

        send_mail(
            subject="New Contact Us request recieved!",
            message=email_message
        )