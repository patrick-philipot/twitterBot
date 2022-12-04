import json
from TwitterAPI import (
    TwitterAPI,
    TwitterPager
)
import keys

client = TwitterAPI(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret, api_version='2')

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