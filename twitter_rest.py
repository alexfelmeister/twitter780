# Credit http://socialmedia-class.org/twittertutorial.html

import io

# Get JSON modules

import csv

try:
    import json
except ImportError:
    import simplejson as json

# import methods from the python "twitter" library

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# import creds variables with my twitter creds in separate settings file

import twittercreds

ACCESS_TOKEN = twittercreds.ACCESS_TOKEN
ACCESS_SECRET = twittercreds.ACCESS_SECRET
CONSUMER_KEY = twittercreds.CONSUMER_KEY
CONSUMER_SECRET = twittercreds.CONSUMER_SECRET

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

# Search for latest tweets about "#braintumorthursday"
braintumorthursday = twitter.search.tweets(q='#BrainTumorThursday', result_type='recent', lang='en', count=10)

f = json.dumps(braintumorthursday, sort_keys=True, indent=2)

print f
file = open("tweets.json", "w")

file.write(f)

file.close()

'''
creates a .csv file using a Twitter .json file
the fields have to be set manually
'''

data_json = open('tweets.json', mode='r').read() #reads in the JSON file into Python as a string
data_python = json.loads(data_json) #turns the string into a json Python object

csv_out = open('tweets_out.csv', mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = ['created_at', 'text', 'screen_name', 'followers', 'friends', 'rt', 'fav'] #field names
writer.writerow(fields) #writes field




    #writes a row and gets the fields from the json object
    #screen_name and followers/friends are found on the second level hence two get methods
'''
    writer.writerow([line.get('created_at'),
                     line.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
                     line.get('user').get('screen_name'),
                     line.get('user').get('followers_count'),
                     line.get('user').get('friends_count'),
                     line.get('retweet_count'),
                     line.get('favorite_count')])
'''
csv_out.close()
