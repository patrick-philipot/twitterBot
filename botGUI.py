'''Twitter API test for Marc'''
import tweepy
import keys
import PySimpleGUI as sg

# Twitter stuff
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

def printFollowers():
    '''Test for Marc'''
    user = api.get_user(screen_name='@DIVIZIO1')
    # Get user Twitter statistics
    print(f"user.followers_count: {user.followers_count}")

    # Show followers
    for follower in user.followers():
        screenName = str(follower.screen_name)
        if screenName[0] in ['a', "A"]:
          print(f'Username:  {screenName}')

def printFollowersCursor():
    '''Another Test for Marc'''
    # the screen_name of the targeted user
    screenName = "@DIVIZIO1"

    # getting only 30 followers
    for follower in tweepy.Cursor(api.get_followers, screen_name = screenName).items(30):
        print(follower.screen_name)

# SimpleGUI stuff
sg.theme("GrayGrayGray")

layout = [[sg.Text("Test Twitter pour Marc")],
          [sg.Button('Followers', key="_FOLL_")],
          [sg.Button('Followers with cursor', key="_CUR1_")],
          [ sg.Stretch(),sg.Button('Fermer la fenêtre', key='_QUIT_', border_width=4)]]

window = sg.Window('Exemple 2 : Event Loop', layout)
#Tweepy init
api = api()

# Event Loop - la fenêtre reste ouverte tant qu'une condition de sortie
# n'est pas atteinte.
while True:
    event, values = window.read()
    # Appui sur le bouton QUIT ou l'icone de fermeture de la fenêtre
    if event == sg.WINDOW_CLOSED or event == '_QUIT_':
        break

    if event ==  '_FOLL_':
        printFollowers()
        break

    if event ==  '_CUR1_':
        printFollowersCursor()
        break

# Ferme la fenêtr et le programme
window.close()
