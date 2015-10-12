#author Rohan Subramaniam

from __future__ import print_function
import json
from TweetInfo import TweetInfo

from TwitterAPI import TwitterAPI
from alchemyapi import AlchemyAPI


CONSUMER_KEY = "LEmiWmBGI2Bnr4dFuKUrgaw3E"
CONSUMER_SECRET = "DaTDMJua3GriyWWlCyFQySeEwabw8plpTPviF8KFOUOEGjqpHn"
ACCESS_TOKEN_KEY = "176509780-cGFgCvxeX9riOUakS4NWWxWbu6I5wmYL97rp9zWz"
ACCESS_TOKEN_SECRET = "qbKgcCPcOr33qatWJQFfr2A1LQpTIHkEUe06YX4pSqIk7"

api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

Team1 = 'Arsenal'
count1 = 50
until = "2015-10-06"
lang = 'en'
geocode1 = "51.5072,0.1275,100mi" #Geocode of london
since = '2015-10-04'

team1_text = ""
team1_list = []
r = api.request('search/tweets', {'lang': lang, 'q': Team1, 'count': count1, 'geocode': geocode1, 'since':since, 'until':until})
for item in r:
    team1_list.append(TweetInfo(item['text'],item['created_at']))
    #print(item['text'])


Team2 = 'Manchester United'
count2 = 50
geocode2 = "53.4667,2.2333,100mi" #geocode of Manchester

team2_text = ""
team2_list = []
r = api.request('search/tweets', {'lang': lang, 'q': Team2, 'count': count2, 'geocode': geocode2, 'since':since, 'until':until})
for item in r:
    team2_list.append(TweetInfo(item['text'],item['created_at']))
    #print(item['text'])

alchemyapi = AlchemyAPI()
sentiment1 = [0.0,0.0]
sentiment2 = [0.0,0.0]

counter1 = 0;
counter2 = 0;

for i in xrange(len(team1_list)):
    response = alchemyapi.sentiment('html', team1_list[i])
    if response['status'] == 'OK':
        response['usage'] = ''
        if 'score' in response['docSentiment']:
            if(float(response['docSentiment']['score']) < 0):
                sentiment[0] += 1
            else:
                sentiment[1] += 1
            #print('positive sentiment score: ', response['docSentiment']['score'])
            counter += 1
    else:
        print('Error in sentiment analysis call: ', response['statusInfo'])
