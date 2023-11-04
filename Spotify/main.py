import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_tracks(username, playlist_id):
    client_credentials_manager = SpotifyClientCredentials(client_id='c5e9be173c5647a79f1d8d16097f0bc5', client_secret='c5ad2986659f4c568850e61a331bdb84')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def get_playlists_by_genre(genres):
    client_credentials_manager = SpotifyClientCredentials(client_id='c5e9be173c5647a79f1d8d16097f0bc5', client_secret='c5ad2986659f4c568850e61a331bdb84')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlists = []
    for genre in genres:
        try:
            results = sp.category_playlists(category_id=genre.strip(), limit=10)
            playlists.extend(results['playlists']['items'])
        except spotipy.exceptions.SpotifyException:
            print(f"Couldn't find any playlists for genre '{genre}'")
    return playlists

# Ask the user for their music preferences
genre = input("What genre of music do you like? ").split(',')

# Get playlists by genre
playlists = get_playlists_by_genre(genre)

# Suggest the first playlist and its tracks
if playlists:
    print("Here's a playlist you might like:")
    print('Playlist Name:', playlists[0]['name'])
    print('Playlist Description:', playlists[0]['description'])
    print('Tracks:')
    tracks = get_playlist_tracks(playlists[0]['owner']['id'], playlists[0]['id'])
    for track in tracks:
        print('-', track['track']['name'])
else:
    print("Sorry, I couldn't find any playlists for that genre.")
