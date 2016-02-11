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
