#!pythonpath
import nytAPI
import parselyAPI

def pullAPIData(artist, title):
  nytData = nytAPI.nytimesData(artist)
  parselyData = parselyAPI.parseLyrics(artist, title)
  print(nytData)
  print(parselyData)
  data = [ nytData[0], nytData[1], parselyData ]
  return data

artist = "Silversun Pickups"
title = "The Royal We"
pullAPIData(artist, title)