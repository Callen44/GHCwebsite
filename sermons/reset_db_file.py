import urllib.request
import json

def reset_db():
    print("reset_db_log: starting")
    # You need to make a file called apinfo.py and add a variable called
    # YOUTUBE_API_KEY, it should be a string and contain the key.
    # This repo is not ment to be deployed by anyone other than the creator
    # do not expect to recive any support!

    # check that there is a key provided
    try:
        from . import apinfo
        key = apinfo.YOUTUBE_API_KEY
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