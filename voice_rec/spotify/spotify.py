# import json
# import spotipy
# import os
# import webbrowser
# import numpy as np

# username = 'erica.nguyen32'
# clientID = 'ae600be297a948a49eddea1447e72d5e'
# clientSecret = '2f638f0f5264430f842a0b8d95e0123a'
# redirect_uri = 'http://localhost/'
# oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
# token_dict = oauth_object.get_access_token()
# token = token_dict['access_token']
# spotifyObject = spotipy.Spotify(auth=token)
# user_name = spotifyObject.current_user()

"""
Prerequisites

    pip3 install spotipy Flask Flask-Session

    // from your [app settings](https://developer.spotify.com/dashboard/applications)
    export SPOTIPY_CLIENT_ID=client_id_here
    export SPOTIPY_CLIENT_SECRET=client_secret_here
    export SPOTIPY_REDIRECT_URI='http://127.0.0.1:8080' // must contain a port
    // SPOTIPY_REDIRECT_URI must be added to your [app settings](https://developer.spotify.com/dashboard/applications)
    OPTIONAL
    // in development environment for debug output
    export FLASK_ENV=development
    // so that you can invoke the app outside of the file's directory include
    export FLASK_APP=/path/to/spotipy/examples/app.py
 
    // on Windows, use `SET` instead of `export`

Run app.py

    python3 app.py OR python3 -m flask run
    NOTE: If receiving "port already in use" error, try other ports: 5000, 8090, 8888, etc...
        (will need to be updated in your Spotify app and SPOTIPY_REDIRECT_URI variable)
"""
#import pyautogui
from tkinter import *
import os
import sys
from flask import Flask, session, request, redirect
from flask_session import Session
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import json
import webbrowser
import numpy as np


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

SPOTIPY_CLIENT_ID='a5ba3a2595154188bc92d807932a7d1c'
SPOTIPY_CLIENT_SECRET='6f6244fdcb304ac986d709ac1feedb7d'
SPOTIPY_REDIRECT_URI='http://localhost:8090'
scope = "user-read-playback-state user-modify-playback-state"

macbook ='9ccb1139563c330086c0758871e1d7210201b0ec'
iphone ='f18bf9d465b761b38a3af2f296db8fcb354de94d'
raspi ='4cac88a0b6d837ba26b5c2f809827e29f94af828'
device_id = np.array( [[macbook], [iphone], [raspi]])
#macbook, iphone, raspberrypi
sp_oauth = SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=scope)


# function to search through json file
def json_full_search(lookup_key, json_dict, search_result=[]):
    if type(json_dict) == dict:
        for key, value in json_dict.items():
            if key == lookup_key:
                search_result.append(value)
            json_full_search(lookup_key, value, search_result)
    elif type(json_dict) == list:
        for element in json_dict:
            json_full_search(lookup_key, element, search_result)
    return search_result

    # will read the track string and find all instances of "name:" and record the following string after that
    # print currently playing track in format of: Artist:_____ Song:________
def printCurrentTrack(temp):
    # format of read names is: "artist name", "album name", "artist name", "song name"
    # the window will remain open until the window is closed

    track_name = None
    track_artist = None
    track_album = None
    #album_cover_url = None
    #count = 0

    with open('track.json', 'w') as fp:
        json.dump(temp, fp)

    data_file = './track.json'
    with open(data_file) as data_file:
        data = json.load(data_file)
        names=json_full_search('name', data)

    track_name = names[3]
    track_artist = names[0]
    track_album = names[1]

    track_list = ['You are currently playing: ', '', track_name, 'by ', track_artist, 'from ', track_album]

    #track = np.array( [['This is what you are listening to \n'],[track_name], [track_artist], [track_album]] )
    # print(track_name, '\n')
    # print(track_artist, '\n')
    # print(track_album, '\n')
    return track_list
    '''
    root = Tk()
    root.title("Current Track")
    root.geometry("300x100")
    artistLabel = Label(root, text='Artist: ' + track_artist).pack()
    trackLabel = Label(root, text='Track: ' + track_name).pack()
    albumLabel = Label(root, text='Album: ' + track_album).pack()
    root.mainloop()
    '''

@app.route('/')
def index():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI, 
                                               scope='user-read-currently-playing playlist-modify-private',
                                               cache_handler=cache_handler,
                                               show_dialog=True)

    if request.args.get("code"):
        # Step 2. Being redirected from Spotify auth page
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/')

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        # Step 1. Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        return f'<h2><a href="{auth_url}">Sign in</a></h2>'

    # Step 3. Signed in, display data
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return f'<h2>Hi {spotify.me()["display_name"]}, ' \
           f'<small><a href="/sign_out">[sign out]<a/></small></h2>' \
           f'<a href="/current_user">me</a> | ' \
           f'<a href="/playlists">my playlists</a> | ' \
           f'<a href="/currently_playing">currently playing</a> | ' \
           f'<a href="/start_playback">start playback</a> | ' \
#           f'<a href="/end_spotify">end spotify</a>' \




@app.route('/sign_out')
def sign_out():
    session.pop("token_info", None)
    return redirect('/')


@app.route('/playlists')
def playlists():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI, 
                                               scope='user-read-currently-playing playlist-modify-private',
                                               cache_handler=cache_handler,
                                               show_dialog=True)
    #auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')

    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return spotify.current_user_playlists()


@app.route('/currently_playing')
def currently_playing():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI, 
                                               scope='user-read-currently-playing playlist-modify-private',
                                               cache_handler=cache_handler,
                                               show_dialog=True)
    #auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    track = spotify.currently_playing()
    if not track is None:
        track = printCurrentTrack(track)
        return '\n'.join(track)

@app.route('/start_playback')
def start_playback():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI, 
                                               #scope='user-read-currently-playing user-modify-playback-state user-read-playback-state',
                                               cache_handler=cache_handler,
                                               show_dialog=True)
    
    #auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        print('here')
        return redirect('/')
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    spotify.start_playback(device_id=macbook)
    return "You are now playing a song" #spotify.start_playback(device_id=raspi)

	

@app.route('/current_user')
def current_user():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, 
                                               client_secret=SPOTIPY_CLIENT_SECRET, 
                                               redirect_uri=SPOTIPY_REDIRECT_URI, 
                                               cache_handler=cache_handler,
                                               show_dialog=True)
    #auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return spotify.current_user()


# @app.route('/end_spotify')
# def end_spotify():
#     pyautogui.press(['ctrl','c'])
#     exit()
    

'''
Following lines allow application to be run more conveniently with
`python app.py` (Make sure you're using python3)
(Also includes directive to leverage pythons threading capacity.)
'''
if __name__ == '__main__':
    app.run(threaded=True, port=int(os.environ.get("PORT",
                                                   os.environ.get("SPOTIPY_REDIRECT_URI", 'http://localhost:8090').split(":")[-1])))

#device id array

device_id = np.array( [ ['f18bf9d465b761b38a3af2f296db8fcb354de94d'],['96dd25fddb7899ed0c54eca8157199ceaf670d1d'], ['9ccb1139563c330086c0758871e1d7210201b0ec'] ] )




