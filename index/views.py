from django.shortcuts import render
from django.http import HttpResponse
from .models import message
from markdown import markdown

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
    return render(request,"contactus.html")