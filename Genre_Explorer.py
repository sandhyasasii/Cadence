import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
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

# Streamlit app structure
st.title("🎶 Genre Explorer")
st.markdown("---")  # Top divider

# List of genres
genres = ['Ambient', 'Electronic', 'Rock', 'Jazz', 'Pop', 'Classical', 'Hip Hop', 'Chill', 'R&B', 'Dance']
genre = st.selectbox("Select a genre to explore:", genres)
st.markdown("---")  # Divider after input

if genre:
    st.subheader(f"Popular Playlists in {genre}")
    st.markdown("---")  # Divider before playlist display

    # Fetch playlists related to the genre
    search_results = sp.search(q=f"{genre}", type='playlist', limit=20)

    if 'playlists' in search_results and 'items' in search_results['playlists']:
        playlists = search_results['playlists']['items']

        for playlist in playlists:
            if playlist:  # Ensure the playlist is not None
                playlist_name = playlist.get('name', 'Unknown Playlist')
                playlist_url = playlist['external_urls']['spotify'] if 'external_urls' in playlist else '#'

                col1, col2 = st.columns([1, 3])  # Adjust column sizes
                with col1:
                    # Check if images exist and use a fallback if not
                    if playlist.get('images') and len(playlist['images']) > 0:
                        image_url = playlist['images'][0]['url']
                        st.image(image_url, width=100)
                    else:
                        st.image("https://via.placeholder.com/100", width=100)  # Fallback image

                with col2:
                    st.write(f"**[{playlist_name}]({playlist_url})**")

                st.markdown("---")  # Divider between playlists

    else:
        st.write(f"Sorry, no playlists found for the genre: {genre}")
        st.markdown("---")  # Divider after no results message
else:
    st.write("Select a genre to explore popular playlists.")
    st.markdown("---")  # Divider if no input
