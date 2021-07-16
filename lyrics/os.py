import os

# Set environment variables
os.environ['SPOTIPY_CLIENT_ID'] = 'id'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'secret'
os.environ['SPOTIPY_REDIRECT_URI'] = 'uri'
os.environ['GENIUS_ACCESS_TOKEN'] = 'token'

# Get environment variables
ID = os.getenv('SPOTIPY_CLIENT_ID')
SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
URI = os.getenv('SPOTIPY_REDIRECT_URI')
TOKEN = os.getenv('GENIUS_ACCESS_TOKEN')
