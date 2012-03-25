#!pythonpath
import re
import urllib
import urllib2
import parseJSON

def getLyrics(artist, title):
  urlBase = "http://www.azlyrics.com/lyrics/"
  artist = artist.lower()
  # Removes spaces from artist name and title
  urlArtist = ""
  for a in artist:
    if (a.isalnum() == True):
      urlArtist += a
  title = title.lower()
  urlTitle = ""
  for a in title:
    if (a.isalnum() == True):
      urlTitle += a
  url = urlBase + urlArtist + "/" + urlTitle + ".html"
  #print(url)
  # GET request to azlyrics
  response = urllib2.urlopen(url)
  html = response.read()
  #print(html)
  return html
  
def removeCrapFromLyrics(lyrics, regex):
  # Uses regex to remove html tags, as well as words inside of [], which
  # break parsely and usually contain useless information like 'Chorus'
  cleanFlag = False
  while (cleanFlag == False):
    match = re.search(regex, lyrics)
    if match:
      #print 'found', match.group()
      #print(match.group())
      lyrics = lyrics.replace(match.group(),"")
      #print(lyrics)
    else:
      #print 'not found'
      cleanFlag = True
  return lyrics

def parselyLyrics(lyrics):
  # Creates url to GET with parsely
  parselyUrl = "http://simon.parsely.com:8983/solr/goldindex2/select/?wt=json&"
  lyricsEncode = { "q" : lyrics }
  lyricsQuery = urllib.urlencode(lyricsEncode)
  parselyUrl += lyricsQuery
  #print(parselyUrl)
  return parselyUrl

def parseLyrics(artist, title):
  source = getLyrics(artist, title)
  result = source.find("<!-- start of lyrics -->")
  # Takes the first 250 characters, including crap we don't need like
  # html tags and [] that are removed after
  lyrics = source[result+24:result+274]
  lyrics = removeCrapFromLyrics(lyrics, "\[.*?\]")
  lyrics = removeCrapFromLyrics(lyrics, "<.*?>")
  # Use parsely to find headlines
  parselyUrl = parselyLyrics(lyrics)
  response = urllib2.urlopen(parselyUrl)
  html = response.read()
  #print(html)
  parselyData = parseJSON.parseJSONlyrics(html)
  
  #print(lyrics)
  return parselyData