import json
from TwitterAPI import (
    TwitterAPI,
    TwitterPager
)

consumer_key        = "<YOUR API KEY>"
consumer_secret     = "<YOUR API KEY SECRET>"
access_token        = "<YOUR ACCESS TOKEN>"
access_token_secret = "<YOUR ACCESS TOKEN SECRET>"


client = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret, api_version='2')


# Get own user id
my_user = client.request(f'users/:me')
USER_ID = my_user.json()['data']['id']


# Getting the Tweet stats
params = {
        "max_results": 100,
        "tweet.fields": "created_at,public_metrics,non_public_metrics,in_reply_to_user_id",
    }
r = client.request(f"users/:{USER_ID}/tweets", params)
tweet_stats = r.json()


# Getting the followers
params = {
        "max_results": 1000,
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


# Get unfollowers/new followers
follower_ids = [follower['id'] for follower in followers]
old_follower_ids = [follower['id'] for follower in old_followers]

new_followers = [follower_id for follower_id in follower_ids if follower_id not in old_follower_ids]
unfollowers = [follower_id for follower_id in old_follower_ids if follower_id not in follower_ids]


# Store followers to file
with open('old_followers.json', 'w') as f:
    json.dump(followers, f)


# Compare old with new followers
if old_followers:
    follower_ids = [follower['id'] for follower in followers]
    old_follower_ids = ['1254777818421932035', '1254777818421932035 FAKE']

    new_followers = [follower_id for follower_id in follower_ids if follower_id not in old_follower_ids]
    unfollowers = [follower_id for follower_id in old_follower_ids if follower_id not in follower_ids]
