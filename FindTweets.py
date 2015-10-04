#author Rohan Subramaniam

from __future__ import print_function
import json
from TweetInfo import TweetInfo

from TwitterAPI import TwitterAPI

#CONSUMER_KEY = "jQ9FwvSr9CGBGn4nXmC3zHslv"
#CONSUMER_SECRET = "AxpPmiGj3lzE1fXoZbvYzc6EyfxiptWuCHgqXjqAKujAoUDce6"
#ACCESS_TOKEN_KEY = "3662721930-AwEAGmxuxzYjIQrKqw5va4k5oD5MU9UL5JSqfg8"
#ACCESS_TOKEN_SECRET = "q5wGgnn7D5Z03epBiMYxri0Xx7LFemCJv26Sidma34LFe"

from TwitterKeys import CONSUMER_KEY,CONSUMER_SECRET, ACCESS_TOKEN_SECRET, ACCESS_TOKEN_KEY

api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

Team1 = 'Arsenal'
count1 = 50
#until = "2015-09-05"
lang = 'en'
geocode1 = "51.5072,0.1275,100mi" #Geocode of london
since = '2015-10-04'
until = ''

team1_text = ""
team1_list = []
r = api.request('search/tweets', {'lang': lang, 'q': Team1, 'count': count1, 'geocode': geocode1, 'since':since})
for item in r:
    team1_list.append(TweetInfo(item['text'],item['created_at']))
    #print(item['text'])


Team2 = 'Manchester United'
count2 = 50
#until = "2015-09-05"
geocode2 = "53.4667,2.2333,100mi" #geocode of Manchester

team2_text = ""
team2_list = []
r = api.request('search/tweets', {'lang': lang, 'q': Team2, 'count': count2, 'geocode': geocode2, 'since':since})
for item in r:
    team2_list.append(TweetInfo(item['text'],item['created_at']))
    #print(item['text'])
