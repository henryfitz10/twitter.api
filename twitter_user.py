import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter
from auth import *


user = get_api().get_user('@madonna')

print (user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print
    print (friend.screen_name)
    print(friend.followers_count)

