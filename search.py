# shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
#This is using client credentials flow
CLIENT_ID = "ae600be297a948a49eddea1447e72d5e"
CLIENT_SECRET = "2f638f0f5264430f842a0b8d95e0123a"

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Olivia Rodrigo'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))
result = sp.search(search_str)
pprint.pprint(result)