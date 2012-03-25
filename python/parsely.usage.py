#!pythonpath

import urllib
import urllib2
import time

# Parse.ly usage
textToParse = "Testing this phrase. What do you think. should be replaced later"
urlBase = "http://hack.parsely.com"
urlParse = urlBase + "/parse?"
text = {"text" : textToParse}

# This encodes into a string with spaces replaced by + (serialized?)
data = urllib.urlencode(text)
req = urllib2.Request(urlParse, data)
response = urllib2.urlopen(req)
parselyJson = response.read()

# Hard code this for now, so I can be lazy and avoid having to regex this
parselyStatus = parselyJson[12:-3]
print(parselyStatus)
urlStatus = urlBase + parselyStatus
status = False
while (status == False):
  response = urllib2.urlopen(urlStatus)
  statusResponse = response.read()
  # Hard coded again...
  if statusResponse[15:-3] == "WORKING":
    print(statusResponse)
    time.sleep(.5)
  else:
    status = True
print(statusResponse)

