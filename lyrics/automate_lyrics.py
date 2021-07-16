import os
import json
import time
import spotipy
import lyricsgenius as lg
from dotenv import load_dotenv


load_dotenv()
ID = os.getenv('SPOTIPY_CLIENT_ID')
SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
URI = os.getenv('SPOTIPY_REDIRECT_URI')
TOKEN = os.getenv('GENIUS_ACCESS_TOKEN')

scope = 'user-read-currently-playing'
oauth_object = spotipy.SpotifyOAuth(client_id=ID, 
                                    client_secret=SECRET, 
                                    redirect_uri=URI, 
                                    scope=scope)
