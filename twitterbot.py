#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time
from random import randint

searchTerms = {
    0: 'music',
    1: 'indie',
    2: 'electronic indie',
    3: 'electronic',
    4: 'rock'
}

CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
ACCESS_KEY = 'YOUR_ACCESS_KEY'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET'


def faveTweets(query):
    print "searching on " + query
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    results = api.search(query)

    for result in results:
        print "  " + result.user.screen_name
        try:
            api.create_favorite(result.id)
        except Exception as ex:
            print "      already favorited"
            
def unFavoriteAll():
    import tweepy, time, sys
    print "deleting all favorites"
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    results = api.favorites()
    while(len(results) > 0):
        for result in results:
            api.destroy_favorite(result.id)
        results = api.favorites()



def executeSomething():
    faveTweets(searchTerms[count % 4])
    print "waiting..."
    print ""
    time.sleep(900)

count = 0
while(count<50):
    executeSomething()
    count += 1
unFavoriteAll()
