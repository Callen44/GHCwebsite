import urllib.request
import json
from .models import apikey
from .models import video as video_data
from googleapiclient.discovery import build
from django.utils.timezone import make_aware
import re  # Import the regular expressions module

def reset_db():
    prep()
    
    # Create a service object for interacting with the YouTube API
    youtube = build('youtube', 'v3', developerKey=key)

    # Make a request to retrieve information about the channel
    response = youtube.channels().list(
        part='contentDetails',
        id=channelID
    ).execute()

    # Extract the playlist ID for the channel's uploaded videos
    playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieve all videos from the playlist
    videos = []
    next_page_token = None

    while True:
        # Make a request to retrieve videos from the playlist
        response = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        # Add the retrieved videos to our list
        videos.extend(response['items'])

        # Check if there are more pages of results
        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    # Process the list of videos and save them to the database
    for video in videos:
        title = video['snippet']['title']
        video_id = video['snippet']['resourceId']['videoId']
        thumbnail_url = video['snippet']['thumbnails']['high']['url']
        youtube_url = f'https://www.youtube.com/watch?v={video_id}'
        publish_date = video['snippet']['publishedAt']

        # Extract the date part from publish_date and format it as 'YYYY-MM-DD'
        publish_date = publish_date.split('T')[0]

        # Use regular expressions to check if "bible" and "study" are together in the title
        if re.search(r'\b(?:bible\s*study|study\s*bible)\b', title, re.IGNORECASE):
            bible_study = True
        else:
            bible_study = False

        # Create an instance of the video model and save it to the database
        new_video = video_data(
            official_name=title,
            date=publish_date,
            thumbnail_url=thumbnail_url,
            biblestudy=bible_study,  # Set the biblestudy field based on the pattern match
            id=video_id
        )
        new_video.save()

        print(f'Saved video: {title}, URL: {youtube_url}, Publish Date: {publish_date}, Bible Study: {bible_study}')

# The rest of your code remains the same


        

def prep():
    global key, channelID

    print("reset_db_log: starting")

    # check if updater is on
    from index.models import system_metatdata

    try:
        metadata = system_metatdata.objects.get(pk=1)
        updator_on = bool(metadata.sermon_updator_on)
    except:
        updator_on = False

    print(updator_on)
    if updator_on != True:
        raise PermissionError('sermon updator is not on, please enable in admin dashboard under system_metadatas')

    # You need to make a file called apinfo.py and add a variable called
    # YOUTUBE_API_KEY, it should be a string and contain the key.
    # This repo is not ment to be deployed by anyone other than the creator
    # do not expect to recive any support!

    # check that there is a key provided
    try:
        key = apikey.objects.first()
        key = str(key.key)
        print("log: key is "+key)
    except:
        raise KeyError('ERROR: youtube API key required!')
    
    channelID = 'UCoMOgaiSCktWEk2CZ7e-aLQ' # this is the @GraceHeritageChurch channel id
    

if __name__ == "__main__":
    reset_db()