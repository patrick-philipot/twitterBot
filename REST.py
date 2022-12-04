import json
from TwitterAPI import (
    TwitterAPI,
    TwitterPager
)

consumer_key        = "xeMASsDEjx9ozYRxUBSq1J2zM"
consumer_secret     = "YlrkBpM64i9tAAaUnM2uABnJ3Hl601rqNPfNloD0qhyppLGbZT"
access_token = '1080801507984003072-n23N9LBNmDkVywVS4gCgLCAoyYqdqq'
access_token_secret = '4dWeQXBhMPgJvM3UYS9oyxFfiADe3LizF4XSDr2AAbyaA'


client = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret, api_version='2')

# Get own user id
my_user = client.request(f'users/:me')
# my_user = client.request(f'users/@DIVIZIO1')
USER_ID = my_user.json()['data']['id']

print(f'USER_ID = {USER_ID}')

# Getting the followers
params = {
        "max_results": 10,
        "user.fields": "id,name,username,created_at,description,profile_image_url,public_metrics,url,verified",
        "user.fields": "id,name,username,created_at,description,profile_image_url,public_metrics,url,verified",
    }
pager = TwitterPager(client, f"users/:{USER_ID}/followers", params)
followers = list(pager.get_iterator())


# Load old followers
try:
    with open('old_followers.json') as f:
        old_followers = json.load(f)
except:
    old_followers = []

# Store followers to file
with open('old_followers.json', 'w') as f:
    json.dump(followers, f)