# spotgpt
Generate music recommendations based on a prompt and create a Spotify playlist with the recommended tracks.



This code is a Python script that generates music recommendations based on a given prompt using OpenAI's GPT-3.5 language model. It then searches for these recommended tracks on Spotify and creates a playlist with the matching tracks. The code uses the Spotipy library for interacting with the Spotify Web API and the OpenAI library for generating recommendations. The Spotify playlist is either created or retrieved if it already exists. The script requires OpenAI and Spotify API credentials, which should be provided in a YAML file. The script accepts command-line arguments for the number of tracks to recommend, the music prompt, and the minimum and maximum BPM (beats per minute) for the recommended tracks. It provides feedback and status updates during the execution, such as generating recommendations, creating/getting the playlist, and adding tracks to the playlist. The resulting playlist details are printed at the end.

Libraries used:

    openai (OpenAI's Python library for API interactions)
    spotipy (Python library for interacting with the Spotify Web API)
    yaml (Python library for working with YAML files)
    json (Python library for working with JSON data)

Prerequisites:

    OpenAI API key: You need to have a valid OpenAI API key to make requests to the OpenAI GPT-3.5 model.
    Spotify API credentials: You need to have valid Spotify API credentials (client ID, client secret, redirect URI) to access the Spotify Web API.
    YAML file: Create a YAML file that contains the necessary credentials for OpenAI and Spotify APIs.

This project requires also OpenAI API key and Spotify API credentials. 

The OpenAI API key is used to generate music recommendations using GPT-3.5 model, and the Spotify API credentials are used to authenticate and interact with the Spotify platform for creating playlists and adding tracks.


Please note that this code is just a starting point and may require additional modifications and configurations based on your specific requirements and environment setup.
