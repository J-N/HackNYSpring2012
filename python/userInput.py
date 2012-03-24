#!pythonpath

import pymongo
import sys
import re

def testMongoDB():
    connection = pymongo.Connection("chipper.bu.edu")
    db = connection.hackny
    db.authenticate("hackny","hackme")
    collection = db.hackNYTest
    collection.insert({'test': 'test'})
    collection.insert({'test': 'test2'})
    print(collection.find()[0])
    print(collection.find()[1])

    collection.remove({'test': 'test'})
    collection.remove({'test': 'test2'})

def getDB():
    connection = pymongo.Connection("chipper.bu.edu")
    db = connection.hackny
    db.authenticate("hackny","hackme")
    collection = db.hackNYTest
    return collection

# Adds the given song to the db returned by getDB()
def addSong(youTubeURL, songTitle, songArtist):
    collection = getDB()
    song = {'URL': youTubeURL, 'Title': songTitle, 'Artist': songArtist}
    print(song)
    collection.insert(song)
    print('inserted song')
    print(collection.find(song)[0])
    
# Removes the given song from the db returned by getDB()
def removeSong(youTubeURL, songTitle, songArtist):
    collection = getDB()
    song = {'URL': youTubeURL, 'Title': songTitle, 'Artist': songArtist}
    print(song)
    collection.remove(song)
    print('removed song')

addSong('http://www.mozart.com','Sonata','Mozart')
addSong('http://www.beethoven.com','Concerto','Beethoven')
removeSong('http://www.mozart.com','Sonata','Mozart')
print(getDB().find_one())
