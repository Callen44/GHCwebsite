def reset_db():
    print("reset_db_log: starting")
    # You need to make a file called apinfo.py and add a variable called
    # YOUTUBE_API_KEY, it should be a string and contain the key.
    # This repo is not ment to be deployed by anyone other than the creator
    # do not expect to recive any support!

    # check that there is a key provided
    try:
        from . import apinfo
        y = apinfo.YOUTUBE_API_KEY
    except:
        raise KeyError('ERROR: youtube API key required!')

    # a valid key is provided, continuing to search youtube for all
    # videos made by the youtube channel @GraceHeritageChurch

    channelID = 'UCoMOgaiSCktWEk2CZ7e-aLQ' # this is the @GraceHeritageChurch channel id