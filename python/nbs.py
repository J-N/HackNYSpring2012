import urllib
import urllib2
import json
import random

def getResponse(urlToSend):
    response = urllib2.urlopen(urlToSend)
    return response.read()

def getArtistID(artistName):
    url = 'http://samjkohn.api3.nextbigsound.com/'\
         +'artists/search.json?q=Kanye'
    response = getResponse(url)
    artist = json.loads(response)
    artistID = artist.keys()[0]
    if artistID == 'status':
        return 0
    #print(artistID)
    return artistID

def getArtistName(artistID):
    url = 'http://samjkohn.api3.nextbigsound.com/'\
          +'artists/view/'+artistID+'.json'
    response = getResponse(url)
    artist = json.loads(response)
    return artist['name']

def getArtistMBID(artistID):
    url = 'http://samjkohn.api3.nextbigsound.com/'\
          +'artists/view/'+artistID+'.json'
    response = getResponse(url)
    artist = json.loads(response)
    return artist['music_brainz_id']

# returns a list of genres associated with the artist
def getArtistGenres(artistID):
    url = 'http://samjkohn.api3.nextbigsound.com/'\
          +'genres/artist/'+artistID+'.json'
    response = getResponse(url)
    genreDict = json.loads(response)
    genreKeys = genreDict.keys()
    genreList = []
    for key in genreKeys:
        genreList.append(genreDict[key]['name'])
    return genreList

# deprecated :-P
def getSimilarArtistsLastFM(artistName, number = 10):
    url = 'http://ws.audioscrobbler.com/2.0/'\
          +'?method=artist.getsimilar&artist='\
          +artistName+'&api_key=6dfbebffcdefdd'\
          +'2771acd4061375bcf6&limit='+number\
          +'&format=json'
    response = getResponse(url)
    similarJSONList = json.loads(response)['similarartists']['artist']
    similarList = []
    for artistDict in similarJSONList:
        similarList.append(artistDict['name'])
    return similarList

# returns the NBS artist ID of similar artists
def getSimilarArtists(artistID, number = 10):
    url = 'http://samjkohn.api3.nextbigsound.com/'\
          +'artists/similar/'+artistID+'.json'
    response = getResponse(url)
    similarDict = json.loads(response)
    return similarDict.keys()[0:number]

# accepts either artist name or id (prefer id)
# isID should be True if artist is the NBS ID
# false if it's the artist's name
def getRandomSongByArtistLastFM(artist, isID):
    songList = getListOfSongsByArtistLastFM(artist, isID)
    index = random.randint(0,len(songList)-1)
    return songList[index]

def getListOfSongsByArtistLastFM(artist, isID):
    limit = 10
    if isID:
        artistParam = 'mbid='\
                      +getArtistMBID(artist)
    else:
        artistParam = 'artist='+artist

    url = 'http://ws.audioscrobbler.com/2.0/?'\
          +'method=artist.gettoptr'\
          +'acks&'+artistParam+'&api_key=6d'\
          +'fbebffcdefdd2771acd4061375bcf6'\
          +'&format=json&limit='+str(limit)
    response = getResponse(url)
    try:
        songJSONList = json.loads(response)\
                   ['toptracks']['track']
    except KeyError:
        return 0
    songList = []
    for songDict in songJSONList:
        songList.append(songDict['name'])
    return songList


    

# to do: rank similar artists by popularity
# to return the most relevant other choices

#for artistID in getRandomSongByArtistLastFM('356', True):
 #  print(getArtistName(artistID))

#print getRandomSongByArtistLastFM('356', True)
