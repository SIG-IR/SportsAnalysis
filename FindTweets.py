#author Rohan Subramaniam

from __future__ import print_function
import json
from TweetInfo import TweetInfo

from TwitterAPI import TwitterAPI


from TwitterKeys import CONSUMER_KEY,CONSUMER_SECRET, ACCESS_TOKEN_SECRET, ACCESS_TOKEN_KEY

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
def list(self, team):
	if team==1:
		return team1_list
	else:
		return team2_list	
