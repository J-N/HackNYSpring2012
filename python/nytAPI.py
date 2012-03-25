#!pythonpath
import urllib
import urllib2
import APIKeys
import parseJSON

def getRequest(URL):
  response = urllib2.urlopen(URL)
  html = response.read()
  return html

def nytimesData():
  # NYTimes api calls:
  # Article Query
  # enter query here. If multiple words, must by connected with a "+"
  artQuery = "test"
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

  # Semantic Person Database
  # Format is "lastname, firstname"
  # This will only work for people, rather than bands...
  # pages (inside of results) is the quantity we are interested in
  semQuery = "West, Kanye"
  semQueryEncode = { "" : semQuery }
  semQueryData = urllib.urlencode(semQueryEncode)
  semAPIKey = APIKeys.getSemAPIKey()
  # From 1 to end, because we need to remove an = that the encode creates and requires
  nytSemanticUrl = "http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_per/" + semQueryData[1:] + ".json?&fields=pages&api-key=" + semAPIKey
  nytSemanticJSON = getRequest(nytSemanticUrl)
  # semantic sets the mode to look for the correct article fields
  # Output is a list full of strings
  semanticData = parseJSON.parseJSONnytimes(nytSemanticJSON, "semantic")
  #print(semanticData)
  
  data = [ articleData, semanticData ]
  return data
  #print(nytSemanticUrl)