# Mongodb instructions
# Most of these things can be named whatever you'd like
connect = pymongo.Connection("chipper.bu.edu")
db = connect.hackny
# can be anything: this makes a hackNYTest test
collection = db.hackNYTest
# example object
test = {'test': 'test'}
collection.insert(test)
# shows back the test 
collection.find()