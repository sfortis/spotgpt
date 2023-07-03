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



How to run:

1. Clone the repository: 
   ```
   git clone https://github.com/your-username/spotgpt.git
   ```
   
2. Navigate to the project directory:
   ```
   cd spotgpt
   ```
   
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   
4. Obtain OpenAI API key:
   - Create an account on the OpenAI website (https://openai.com/).
   - Generate an API key from your OpenAI account dashboard.
   - Copy the API key and replace the placeholder in `secrets.yaml` file with your actual API key.
   
5. Obtain Spotify API credentials:
   - Create a Spotify Developer account (https://developer.spotify.com/).
   - Create a new Spotify application and note down the Client ID and Client Secret.
   - Set the Redirect URI to `http://localhost:8000/callback` in your Spotify application settings.
   - Replace the placeholders in `secrets.yaml` file with your Spotify API credentials and desired username.
   
6. Run the application:
   ```
   python spotgpt.py <num_of_tracks> <music_prompt> <min_bpm> <max_bpm>
   ```
   - `<num_of_tracks>`: Number of tracks to recommend and add to the playlist.
   - `<music_prompt>`: Prompt defining the playlist tracks.
   - `<min_bpm>`: Minimum BPM (beats per minute) for the recommended tracks.
   - `<max_bpm>`: Maximum BPM (beats per minute) for the recommended tracks.

   For example:
   ```
   python spotgpt.py 10 "Pink Floyd covers" 80 120
   ```

7. Follow the instructions on the console:
   - The application will generate music recommendations based on the provided prompt.
   - It will create a new Spotify playlist or use an existing one with the same name as the music prompt.
   - The recommended tracks will be searched on Spotify and added to the playlist.
   - The playlist details will be displayed at the end.

Note: Make sure you have Python installed on your system before running the application. Also, ensure that the required keys and credentials are correctly configured in the `secrets.yaml` file.



Please note that this code is just a starting point and may require additional modifications and configurations based on your specific requirements and environment setup.
