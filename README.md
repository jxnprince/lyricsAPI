# SpotifyLyricsAPI

•NOTE: This guide assumes the user has Python3 installed on their machine.

## Setup instructions

•Clone this repo `git clone https://github.com/jxnprince/lyricsAPI.git`

•Create your VENV `python3 -m venv << NAME OF VENEV >>`

•Install dependencies `pip install spotipy lyricsgenius`

•Create a `.env` file at the root level and copy the supplied Environment Variables from the email sent you by Jackson Prince and paste them into your newly created .env module & be sure to save!

•Open the Spotify desktop client and play a track of your choice

### Authentication steps (This is only required once):
•Now run `python automate_lyrics.py` in your terminal from the 'lyricsAPI-main' directory

•This will automatically redirect you to Google with an augmented URL.  Copy the entire URL and return to your terminal.

•Your terminal should read `Enter the URL you were redirected to: `

•Paste the previously copied Google URL and submit.  You can now close your browser window.

•If you do not have anything currently playing in Spotify you will get an error: `TypeError: 'NoneType' object is not subscriptable`. If you come across this error the process with automatically cancel.  Be sure to have a track playing before running the script.
