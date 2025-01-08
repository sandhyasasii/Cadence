import random
from keybert import KeyBERT
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Spotify credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Spotify API setup
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# KeyBERT setup
kw_model = KeyBERT()

# Streamlit app structure
st.markdown(
    "<h1 style='color: #961822; text-align: center; font-size: 3em;'>♪ Custom Playlist Generator</h1>",
    unsafe_allow_html=True,
)

st.markdown("---")

# User Input
prompt = st.text_area("Describe your ideal playlist (mood, genre, themes):", "")

# Function to fetch playlists from Spotify
def fetch_playlists(query, limit=10):
    results = sp.search(q=query, type='playlist', limit=limit)
    return results.get('playlists', {}).get('items', [])

# Function to fetch random tracks from playlists
def get_random_tracks(playlists, num_tracks=10):
    all_tracks = []
    for playlist in playlists:
        # Ensure the playlist is valid and contains an 'id'
        if playlist and 'id' in playlist:
            playlist_id = playlist['id']
            tracks = sp.playlist_tracks(playlist_id, fields="items.track")
            if 'items' in tracks:
                all_tracks.extend(
                    [track['track'] for track in tracks['items'] if track.get('track')]
                )
    # Return random selection of tracks
    if all_tracks:
        return random.sample(all_tracks, min(num_tracks, len(all_tracks)))
    else:
        return []  # Return empty list if no tracks found

# Main Playlist Generation Logic
if prompt:
    with st.spinner("Generating playlist..."):
        # Step 1: Search Spotify with the full prompt
        playlists = fetch_playlists(prompt)

        if not playlists:
            # Step 2: Fallback to keyword extraction if no playlists found
            st.warning("No playlists found for the full prompt. Extracting keywords...")
            keywords = kw_model.extract_keywords(prompt, keyphrase_ngram_range=(1, 2), stop_words="english", top_n=5)
            keyword_queries = [kw[0] for kw in keywords]  # Extract only the keyword strings

            # Collect playlists for each keyword
            playlists = []
            for keyword in keyword_queries:
                playlists.extend(fetch_playlists(keyword))

        # Step 3: Fetch random tracks from collected playlists
        tracks = get_random_tracks(playlists)

    # Display the generated playlist
    if tracks:
        st.success("Playlist generated!")
        st.markdown("**Your Custom Playlist:**")
        for track in tracks:
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            album_cover_url = track['album']['images'][0]['url']
            track_url = track['external_urls']['spotify']

            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(album_cover_url, width=100)
            with col2:
                st.write(f"**{track_name}** by {artist_name}")
                st.markdown(f"[🎧 Listen on Spotify]({track_url})")
            st.markdown("---")  # Divider between tracks
    else:
        st.error("Sorry, no tracks found for your prompt.")
