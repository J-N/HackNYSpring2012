#!pythonpath
import urllib
import urllib2
import APIKeys
import parseJSON
import re

def getRequest(URL):
  response = urllib2.urlopen(URL)
  html = response.read()
  return html

def nytimesData(artist):
  # NYTimes api calls:
  # Article Query
  # enter query here. If multiple words, must by connected with a "+", but 
  # urlencode takes care of this
  artist = artist.lower()
  artQuery = artist
  artQueryEncode = { "query" : artQuery }
  artQueryData = urllib.urlencode(artQueryEncode)
  artAPIKey = APIKeys.getArtAPIKey()
  nytArticleUrl = "http://api.nytimes.com/svc/search/v1/article?format=json&" + artQueryData + "&fields=title,url,date&api-key=" + artAPIKey
  nytArticleJSON = getRequest(nytArticleUrl)
  # article sets the mode to look for the correct article fields
  # Output is a list full of strings
  articleData = parseJSON.parseJSONnytimes(nytArticleJSON, "article")
  #print(articleData)
  #print('\n\n')
  
  # Finding people sucks, so we're not dealing with it right now. See person.nyt.temp.py for the code
  semanticData = 0
  
  data = [ articleData, semanticData ]
  return data
  #print(nytSemanticUrl)