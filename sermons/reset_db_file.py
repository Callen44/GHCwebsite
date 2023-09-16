import urllib.request
import json
from .models import apikey, video

def reset_db():
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

    # a valid key is provided, continuing to search youtube for all
    # videos made by the youtube channel @GraceHeritageChurch

    channelID = 'UCoMOgaiSCktWEk2CZ7e-aLQ' # this is the @GraceHeritageChurch channel id
    request_url = "https://www.googleapis.com/youtube/v3/search?key="+key+"&channelId="+channelID+"&part=snippet,id&order=date"

    print(request_url)
    print("log: making request - " + request_url)
    with urllib.request.urlopen(request_url) as response:
        data = json.loads(response.read().decode())
        print(data)

if __name__ == "__main__":
    reset_db()