from __future__ import annotations
import streamlit as st
from memoryfm.streamlit.util import PADDING


st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title(":primary[memory.fm]")
"##### *music meets memory*"
"---"


st.markdown("""
**memory.fm** is a tool for exploring your music listening history from Last.fm and Spotify.

Instead of focusing only on aggregate stats, it surfaces long-term and local patterns such as attachment, repetition, 
and obsessive listening, to help you revisit periods of your life through music.

*✨ :grey[Inspired by the idea of using music as a way to revisit memories] ✨*
""")

st.markdown("""
### Stats and Visuals
[**:material/list_alt: Overview**](overview) -- A summary of listening history.  
[**:material/bar_chart: Top Charts**](top_charts) -- The top artists, albums, and tracks by period.  
[**:material/person_heart: Attachment Index**](attachment) -- How concentrated your listening was on particular artists, albums, or tracks.  
[**:material/bolt: Streaks**](streaks) -- The periods of obsessive listening.  
""")

