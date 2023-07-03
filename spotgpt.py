import openai
import sys
import yaml
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def load_openai_api_key(file_path):
    with open(file_path) as file:
        secrets = yaml.safe_load(file)
        return secrets["openai_api_key"]


def load_spotify_credentials(file_path):
    with open(file_path) as file:
        secrets = yaml.safe_load(file)
        return secrets["spotify"]


def generate_recommendation(num_of_tracks, music_prompt, min_bpm, max_bpm):
    # Set up your OpenAI API credentials
    api_key = load_openai_api_key("/users/sfortis/secrets.yaml")
    openai.api_key = api_key

    prompt = f'Recommend {music_prompt} music. You should provide {num_of_tracks} tracks. BPM should be between {min_bpm} and {max_bpm}.'

    # Generate a response using OpenAI GPT-3.5
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "system", "content": "You are an AI helpful DJ assistant with great knowledge of music."},
            {"role": "system", "content": "Always reply with a JSON array named 'tracks' with the only objects 'track' for the song name and 'artist' for the artist name."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=1,
        n=1,
        stop=None,
    )

    # Extract the recommended tracks from the response
    tracks = response.choices[0].message.content.strip()

    return tracks


def create_spotify_playlist(music_prompt, spotify_credentials):
    # Set up your Spotify API credentials
    client_id = spotify_credentials["client_id"]
    client_secret = spotify_credentials["client_secret"]
    username = spotify_credentials["username"]
    redirect_uri = spotify_credentials["redirect_uri"]
    scope = "playlist-modify-public"

    # Authenticate with Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                                   redirect_uri=redirect_uri, scope=scope, username=username))

    # Check if the playlist already exists
    playlists = sp.current_user_playlists()
    for playlist in playlists["items"]:
        if playlist["name"] == f"AI playlist - {music_prompt}":
            return playlist

    # Create a new playlist if it doesn't exist
    playlist_name = f"AI playlist - {music_prompt}"
    playlist = sp.user_playlist_create(user=username, name=playlist_name, public=True)

    return playlist


def search_track_on_spotify(track_name, artist_name, sp):
    # Construct the query
    query = f'track:{track_name} artist:{artist_name}'

    # Search for a track on Spotify using the query
    results = sp.search(q=query, type='track', limit=1)

    if len(results['tracks']['items']) > 0:
        return results['tracks']['items'][0]['uri']
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) < 5:
        # Display help text if not enough arguments are provided
        print("Usage: python spotgpt.py <num_of_tracks> <music_prompt> <min_bpm> <max_bpm>")
        print("Parameters:")
        print("<num_of_tracks>   : Number of tracks to recommend and add to the playlist (integer)")
        print("<music_prompt>    : Prompt defining the playlist tracks (string)")
        print("<min_bpm>         : Minimum BPM (beats per minute) for the recommended tracks (integer)")
        print("<max_bpm>         : Maximum BPM (beats per minute) for the recommended tracks (integer)")
        sys.exit(0)

    # Continue with the rest of the code if the arguments are provided
    num_of_tracks = int(sys.argv[1])
    music_prompt = sys.argv[2]
    min_bpm = int(sys.argv[3])
    max_bpm = int(sys.argv[4])

    # Load OpenAI API key
    openai_api_key = load_openai_api_key("/users/sfortis/secrets.yaml")
    openai.api_key = openai_api_key

    # Call the recommendation function
    print("Generating music recommendations...")
    recommended_tracks = generate_recommendation(num_of_tracks, music_prompt, min_bpm, max_bpm)
    print("Music recommendations generated.")

    try:
        # Parse the recommended tracks from the JSON object
        tracks_json = json.loads(recommended_tracks)["tracks"]
    except json.JSONDecodeError as e:
        print("Error: Failed to parse the JSON response.")
        print(e)
        sys.exit(1)

    if len(tracks_json) == 0:
        print("No songs found. Exiting.")
        sys.exit(0)

    # Load Spotify credentials
    spotify_credentials = load_spotify_credentials("/users/sfortis/secrets.yaml")

    # Authenticate with Spotify and create or get the existing playlist
    print("Creating/Getting a Spotify playlist...")
    playlist = create_spotify_playlist(music_prompt, spotify_credentials)
    print("Spotify playlist created/found.")

    # Authenticate with Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_credentials["client_id"],
                                                   client_secret=spotify_credentials["client_secret"],
                                                   redirect_uri=spotify_credentials["redirect_uri"],
                                                   scope="playlist-modify-public",
                                                   username=spotify_credentials["username"]))

    # Iterate through the tracks and search on Spotify
    print("Adding tracks to the playlist...")
    added_tracks = 0  # Variable to keep track of added tracks
    for i, track in enumerate(tracks_json, 1):
        track_name = track['track']
        artist_name = track['artist']

        # Search for the track on Spotify
        track_uri = search_track_on_spotify(track_name, artist_name, sp)

        if track_uri:
            # Add the track to the playlist
            sp.playlist_add_items(playlist['id'], [track_uri])
            added_tracks += 1  # Increment the count of added tracks
            print(f"Added track {added_tracks}/{num_of_tracks} to the playlist.")

            # Check if the required number of tracks has been added
            if added_tracks == num_of_tracks:
                break

    # Print the playlist details
    print(f"Playlist '{playlist['name']}' created on Spotify with {added_tracks} tracks.")
