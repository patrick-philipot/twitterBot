import tweepy
import keys


def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted successfully!')


if __name__ == '__main__':
    api = api()
    # tweet(api, 'This was tweeted from Python', 'cat.png')
    user = api.get_user(screen_name='@DIVIZIO1')

    # Get user Twitter statistics
    print(f"user.followers_count: {user.followers_count}")

    # Show followers
    for follower in user.followers():
        #print('Name: ' + str(follower.name))
        print('Username: ' + str(follower.screen_name))