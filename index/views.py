from django.shortcuts import render
from django.http import HttpResponse
from .models import message
from markdown import markdown

# Create your views here.

def index(request):
    messages = message.objects.get(pk=1)
    visiontitle = messages.ourvisiontitle
    print(visiontitle)
    return render(request,"index.html", {"visiontitle":visiontitle})

def ourvision(request):
    messages = message.objects.get(pk=1)
    messages = markdown(str(messages.ourvision))
    return render(request,"aboutus.html", {"Vision":messages})