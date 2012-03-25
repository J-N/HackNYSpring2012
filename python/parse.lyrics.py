#!pythonpath
import re
import urllib
import urllib2

def getLyrics(artist, title):
  urlBase = "http://www.azlyrics.com/lyrics/"
  artist = artist.lower()
  artist = re.findall("\w*",artist)
  urlArtist = artist[0]+artist[2]
  title = title.lower()
  urlTitle = ""
  for a in title:
    if (a.isalnum() == True):
      urlTitle += a
  url = urlBase + urlArtist + "/" + urlTitle + ".html"
  response = urllib2.urlopen(url)
  html = response.read()
  #print(html)
  return html
  
def removeCrapFromLyrics(lyrics, regex):
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
  parselyUrl = "http://simon.parsely.com:8983/solr/goldindex2/select/?wt=json&"
  lyricsEncode = { "q" : lyrics }
  lyricsQuery = urllib.urlencode(lyricsEncode)
  parselyUrl += lyricsQuery
  print(parselyUrl)
  return parselyUrl

def parseLyrics():
  source = getLyrics("Kanye West", "Stronger")
  result = source.find("<!-- start of lyrics -->")
  lyrics = source[result+24:result+274]
  lyrics = removeCrapFromLyrics(lyrics, "\[.*?\]")
  lyrics = removeCrapFromLyrics(lyrics, "<.*?>")
  parselyUrl = parselyLyrics(lyrics)
  response = urllib2.urlopen(parselyUrl)
  html = response.read()
  print(html)
  
  #print(lyrics)
  #return(lyrics)
  
parseLyrics()