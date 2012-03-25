#!pythonpath
import nytAPI
import parselyAPI

def pullAPIData():
  nytData = nytAPI.nytimesData()
  parselyData = parselyAPI.parseLyrics()
  
pullAPIData()