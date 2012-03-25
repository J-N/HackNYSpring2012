#!pythonpath
import urllib
import urllib2
import APIKeys

# NYTimes api calls:
# Article Query
# enter query here. If multiple words, must by connected with a "+"
artQuery = "test"
artQueryEncode = { "query" : artQuery }
artQueryData = urllib.urlencode(artQueryEncode)
artAPIKey = APIKeys.getArtAPIKey()
nytArticleUrl = "http://api.nytimes.com/svc/search/v1/article?format=json&" + artQueryData + "&fields=title,url,date&api-key=" + artAPIKey
print(nytArticleUrl)

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
print(nytSemanticUrl)

# Get request
response = urllib2.urlopen(nytSemanticUrl)
html = response.read()
print(html)

# Post Request
#url = "http://hack.parsely.com/parse?"
#text = {"text" : "Hello World"}
# This encodes into a string with spaces replaced by + (serialized?)
#data = urllib.urlencode(text)
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#page = response.read()
#print(page)

