from django.shortcuts import render
from django.http import HttpResponse
from .models import message

# Create your views here.

def index(request):
    return render(request,"index.html", {"blank":"hi"})

def ourvision(request):
    messages = message.objects.get(pk=1)
    print(messages.ourvision)
    return render(request,"ourvision.html", {"Vision":messages.ourvision})