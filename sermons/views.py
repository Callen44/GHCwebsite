from django.shortcuts import render
from . import models

# Create your views here.
def index(request):

    # get videos from the django datbase
    videos = models.video.objects.all().order_by("-date")

    # reformat them so that they are easier to work within the template
    formatted_videos = []

    for video in videos:
        formatted_videos.append({"id":video.id, "title":video.official_name,"biblestudy":video.biblestudy, "thumbnail":video.thumbnail_url, "date": video.date})

    print(formatted_videos)

    return render(request,'sermons.html',{'videos':formatted_videos})