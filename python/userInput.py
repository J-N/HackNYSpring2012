#!pythonpath

import pymongo

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

# Gets the db.hackny.hackNYTest database
def getDB():
    connection = pymongo.Connection("chipper.bu.edu")
    db = connection.hackny
    db.authenticate("hackny","hackme")
    collection = db.hackNYTest
    return collection

# Returns True if the given youTubeURL is already in the database
def isSongInDB(youTubeURL):
    collection = getDB()
    count = collection.find({'URL': youTubeURL}).count()
    if count == 0:
        return False
    else:
        return True


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

def getSongID(youTubeURL):
    collection = getDB()
    _id = collection.find_one({'URL': youTubeURL}, {'_id': 1})
    if _id == None:
        print("damn it no such song exists: " + youTubeURL)
        return 0
    else:
        return _id


def testAddSong():
    collection = getDB()
    addSong('http://www.mozart.com','Sonata','Mozart')
    addSong('http://www.beethoven.com','Concerto','Beethoven')
    print(collection.find_one(collection.find({'Title':'Sonata'})[0]))
    removeSong('http://www.mozart.com','Sonata','Mozart')
    print(getDB().find_one())

# returns a json formatted game containing the song urls provided
# the songs are stored by _id: Song1_ID, Song2_ID, etc.
# the each user can have only 1 game with a given game name
def getGame(userName, gameName, song1, song2, song3, song4, song5):
    game = {'UserName': userName, \
            'GameName': gameName, \
            'Song1_ID': getSongID(song1), \
            'Song2_ID': getSongID(song2), \
            'Song3_ID': getSongID(song3), \
            'Song4_ID': getSongID(song4), \
            'Song5_ID': getSongID(song5)}
    return game

# adds the game to the database
def insertGame(game):
    collection = getDB()
    collection.insert(game)

# prints all the entries of the database
def printDB():
    collection = getDB()
    cursor = collection.find()
    count = cursor.count()
    for i in range(0,count):
        print(cursor[i])

#printDB()
#print(getSongID('http://www.beethoven.com'))
#print(getSongID('http://www.mozart.com'))
#print(isSongInDB('http://www.beethoven.com'))
#print(isSongInDB('http://www.mozart.com'))
