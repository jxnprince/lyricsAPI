# SpotifyLyricsAPI

•NOTE: This guide assumes the user has Python3 installed on their machine.

## Setup instructions

•Clone this repo with `git clone https://github.com/jxnprince/lyricsAPI.git`

•Be sure your current working directory is the root directory of this repo and run `touch .env`

•Copy the supplied Environment Variables from the email sent you by Jackson Prince and paste them into your newly craeted .env module & be sure to save!

•Open the Spotify desktop client and play a track of your choice

### Authentication steps (This is only required once):
•Now run `python automate_lyrics.py` in your terminal from the 'lyricsAPI-main' directory

•This will automatically redirect you to Google with an augmented URL.  Copy the entire URL and return to your terminal.

•Your terminal should read `Enter the URL you were redirected to: `

•Paste the previously copied Google URL.

•If you do not have anything currently playing in Spotify you will get an error: `TypeError: 'NoneType' object is not subscriptable`. If you come across this error the process with automatically cancel.  Be sure to have a track playing before running the script.
