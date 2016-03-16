import json
import tweepy
from tweepy import OAuthHandler
from auth import *

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = get_api().trends_place(DUB_WOE_ID)
lon_trends = get_api().trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                        for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print common_trends




