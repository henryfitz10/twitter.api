import json
from auth import *


count = 10
query = 'dublin'

#Get all status
results = [status for status in tweepy.Cursor(get_api().search, q= query).items(count)]

for result in results:
    print json.dumps(results[0]._json, indent=4)

for status in results:
    print status.text.encode('utf-8')
    print status.user.id
    print status.user.screen_name
    print status.user.profile_image_url_https
    print status.user.followers_count
    print status.place

