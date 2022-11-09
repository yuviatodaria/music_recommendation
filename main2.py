import re
import os
import spotipy
import pandas as pd
from dotenv import load_dotenv
from collections import defaultdict
from spotipy.oauth2 import SpotifyClientCredentials
from multiprocessing.pool import ThreadPool as Pool
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

load_dotenv()

spotify_client_id = os.getenv('CLIENT_ID')
spotify_client_secret = os.getenv('CLIENT_SECRET')

spotify = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))

# fetching the information regarding the track that user entered
def multiple_tracks():
    song_name="hardum humdum"
    song_artist = "arijit singh"
    result = spotify.search(q='track: {} artist: {}'.format(song_name, song_artist), limit=5)
    # print(result)

    # not able to find song (return None)
    if result['tracks']['items'] == []:
        return None

    # s_id = result['tracks']['items'][0]['id']
    # s_trackname = result['tracks']['items'][0]['name']
    # s_popularity = result['tracks']['items'][0]['popularity']
    # s_artist = result['tracks']['items'][0]['album']['artists'][0]['name']
    # s_img = result['tracks']['items'][0]['album']['images'][0]['url']
    # s_url = result['tracks']['items'][0]['external_urls']['spotify']

    for i in range(0,5):
        s_id = result['tracks']['items'][i]['id']
        s_trackname = result['tracks']['items'][i]['name']
        s_artist = result['tracks']['items'][i]['album']['artists'][0]['name']
        s_img = result['tracks']['items'][i]['album']['images'][0]['url']
        s_year = result['tracks']['items'][i]['album']['release_date']
        s_popularity = result['tracks']['items'][i]['popularity']
        s_url = result['tracks']['items'][i]['external_urls']['spotify']
        print(s_id,s_trackname,s_popularity,s_artist,s_img,s_url,s_year)


    # retrieving the user tracks features from spotify api
    # track_info = spotify.audio_features(tracks=s_id)
    # track_info = track_info[0]

    # track_data = defaultdict()
    # for key, value in track_info.items():
    #     track_data[key] = value

    # print(track_data)

    return 0

if __name__ == '__main__':
    multiple_tracks()