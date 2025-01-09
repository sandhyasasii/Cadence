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
redirect_uri = 'http://localhost:5000/Top_Tracks'

# Spotify OAuth setup
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                               client_secret=client_secret,
                                               
                                            #    scope="user-library-read user-top-read"
                                            ))

# List of genres (adjust as needed)
available_genres = [
    'Ambient', 'Electronic', 'Psychedelic', 'Space Rock', 'Progressive Rock', 'Chillwave',
    'Synthwave', 'Trance', 'Cosmic Jazz', 'Space Disco'
]

# Page Configuration
st.set_page_config(
    page_title="Top Tracks on Spotify",
    page_icon="🎵",
    layout="centered",
)

st.title("🎵 Discover Top Tracks by Genre")
st.markdown("---")  # Add a separator line

st.subheader("Search for a Genre")
genre = st.text_input("Enter a genre:", "").strip()



# Fetch top tracks for the selected genre
def get_top_tracks_for_genre(genre):
    query = f"genre:{genre}"
    
    # Fetch top tracks for the genre
    results = sp.search(q=query, limit=10, type='track')
    
    return results['tracks']['items']

if genre:
    # Display top tracks for selected genre
    st.write(f"**Top Tracks in {genre}**:")

    # Get tracks for the selected genre
    top_tracks = get_top_tracks_for_genre(genre)

    if top_tracks:
        for track in top_tracks:
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            album_cover_url = track['album']['images'][0]['url']
            track_url = track['external_urls']['spotify']

            col1, col2 = st.columns([1, 3])  # Adjust column sizes
            with col1:
                st.image(album_cover_url, width=100)  # Album cover
            with col2:
                st.write(f"**{track_name}** by {artist_name}")
                st.markdown(f"[🎧 Listen on Spotify]({track_url})")

            st.markdown("---")  # Divider between tracks

    else:
        st.write(f"Sorry, no results found for the genre: {genre}")
