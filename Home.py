# import streamlit as st
# import streamlit.components.v1 as com



# st.set_page_config(
#     page_title="Cadence",
#     page_icon="🎧",
# )



# st.markdown("<h1 style='color: #961822;'>Welcome to Cadence</h1>", unsafe_allow_html=True)

# st.sidebar.success("~ select a topic above to browse ~")

# st.markdown(
#     """
#     Cadence is an engaging web application that allows users to explore and analyze their music taste through Spotify. 
#     With insightful visualizations and interactive features, Cadence provides a personalized overview of your music preferences, giving you a deeper understanding of your listening habits.
#     **Select a view from the sidebar** to see your music analytics.
#     """
# )

# com.iframe("https://lottie.host/embed/c2162be1-aec3-4ae1-8766-fd925601d796/EPSTrCa9qu.lottie")

import streamlit as st
import streamlit.components.v1 as com

# Page Configuration
st.set_page_config(
    page_title="Cadence",
    page_icon="🎧",
    layout="centered",
)

# Sidebar Message
st.sidebar.success("~ Select a topic above to browse ~")

# Main Title with Style
st.markdown(
    "<h1 style='color: #961822; text-align: center; font-size: 3em;'>Welcome to Cadence 🎵</h1>",
    unsafe_allow_html=True,
)

# Layout Columns for Animation and Intro Text
col1, col2 = st.columns([1, 2])

with col1:
    # Lottie Animation
    #com.iframe("https://lottie.host/embed/51444e0a-234f-4dc2-8535-790a7c20655c/9KHCaqL1mL.lottie", height=100, width=200)
    com.iframe("https://lottie.host/embed/c2162be1-aec3-4ae1-8766-fd925601d796/EPSTrCa9qu.lottie", height=200, width=200)
    


with col2:
    # Introductory Text
    st.markdown(
        """
        <div style='font-size: 1.2em; line-height: 1.8;'>
       Cadence is an engaging web application that allows users to explore music Spotify. 
       With features like genre-based playlist discovery and top track exploration, Cadence helps users uncover new music and popular playlists in their favorite genres, providing an engaging and visually appealing way to dive into the world of music.
        <br><br>
        <b>✨ Select a page from the sidebar ✨</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Add a Horizontal Divider
st.markdown("<hr style='border:1px solid #961822; margin: 20px 0;'>", unsafe_allow_html=True)


# Add Footer
st.markdown(
    "<div style='text-align: center; margin-top: 20px;'>"
    "Built with ❤️ for music lovers.</div>",
    unsafe_allow_html=True,
)

# # Importing Streamlit
# import streamlit as st

# # Define HTML and CSS for the tooltip
# html_content = """
# <style>
# .tooltip {
#   position: relative;
#   display: inline-block;
#   cursor: pointer;
# }

# .tooltip .tooltiptext {
#   visibility: hidden;
#   width: 120px;
#   background-color: black;
#   color: white;
#   text-align: center;
#   border-radius: 6px;
#   padding: 5px 0;
#   position: absolute;
#   z-index: 1;
#   top: 100%;
#   left: 50%;
#   margin-left: -60px;
#   opacity: 0;
#   transition: opacity 0.3s;
# }

# .tooltip:hover .tooltiptext {
#   visibility: visible;
#   opacity: 1;
# }
# </style>

# <div class="tooltip">
#   <img src="https://cdn.vox-cdn.com/thumbor/WR9hE8wvdM4hfHysXitls9_bCZI=/0x0:1192x795/1400x1400/filters:focal(596x398:597x399)/cdn.vox-cdn.com/uploads/chorus_asset/file/22312759/rickroll_4k.jpg" alt="Image" style="width:200px;height:auto;">
#   <span class="tooltiptext">Tooltip text</span>
# </div>
# """

# # Display HTML in Streamlit
# st.markdown(html_content, unsafe_allow_html=True)