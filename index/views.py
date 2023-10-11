from django.shortcuts import render
from django.http import HttpResponse
from .models import message, contact_request
from markdown import markdown
from .tasks import email_pastors_new_message
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request,"index.html")

def ourvision(request):
    messages = message.objects.get(pk=1)
    messages = markdown(str(messages.ourvision))
    return render(request,"aboutus.html", {"Vision":messages})

def visit(request):
    messages = message.objects.get(pk=1)
    messages = markdown(str(messages.visitmessage))
    return render(request,"visit.html", {"Visit":messages})

def contactus(request):
    # check if there is any data in the request, then notify the template if it sould show an alert

    # name or email can't be too long (1000 characters) if there is no post data then don't even bother checking it
    
    # Use try to figure out if there even is any data
    
    try:
        # if name and email were detected in the post data then this code will be successful
        blank = request.POST['name']
        blank = request.POST['email']
        blank = request.POST['message']
    except:
       # there was no data coming in, send the template to the user with no message
        return render(request,"contactus.html", {"Message":None, "Success":None})

    # the data was found so we are loading it into the database and scheduling a task to run on celery for notifying pastory
    msg = None
    success = None

    # add the contact request to that database and make sure that no error are raised if no data is returned
    try:
        new_contact_request = contact_request(
            name = request.POST['name'],
            email = request.POST['email'],
            message = request.POST['message'],
        )
        new_contact_request.save()
        msg = "Success! it may take 5-10 minutes for the pastors to be notified."
        success = True
    except:
        pass

    # schedule a task for the pastors to recieve an email
    email_pastors_new_message.apply_async(eta=timezone.now())

    return render(request,"contactus.html", {"Message":msg,"Success":success})