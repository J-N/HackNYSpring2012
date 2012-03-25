import urllib
import urllib2
import json

def getResponse(urlToSend):
    response = urllib2.urlopen(urlToSend)
    return response.read()

def getArtistID(artistName):
    url = 'http://samjkohn.api3.nextbigsound.com/'\
         +'artists/search.json?q=Kanye'
    response = getResponse(url)
    artist = json.loads(response)
    artistID = artist.keys()[0]
    #print(artistID)
    return artistID

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

def getSimilarArtists(artistName):
    url = 'http://ws.audioscrobbler.com/2.0/'\
          +'?method=artist.getsimilar&artist='\
          +artistName+'&api_key=6dfbebffcdefdd'\
          +'2771acd4061375bcf6&limit=5&format=json'
    response = getResponse(url)
    print response
    similarList = json.loads(response)['similarartists']['artist']
    for artistDict in similarList:
        print(artistDict['name'])

#for genre in getArtistGenres(getArtistID('Kanye')):
 #  print(genre)

print getSimilarArtists('kanye')
