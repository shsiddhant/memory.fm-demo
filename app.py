from __future__ import annotations
import streamlit as st
from util import set_session_data
from pathlib import Path
from index import (
    home,
    overview,
    attachment,
    top_charts,
    streaks
)
from config import USERNAME
PATH = Path("data").resolve() / USERNAME

st.set_page_config(layout="wide")

if "username" not in st.session_state:
    st.session_state["username"] = USERNAME
if "sc_log" not in st.session_state:
    st.session_state["sc_log"] = None

set_session_data(USERNAME)

if st.session_state.get("sc_log"):
    pages = [
        home,
        overview,
        top_charts,
        attachment,
        streaks
    ]
    pg = st.navigation(pages)
    with st.sidebar:
        st.markdown("**Links**")
        st.markdown(
            "[![Github Repo](https://img.shields.io/badge/Github-black?logo=github&style=plastic)]"
            "(https://github.com/shsiddhant/memory.fm/)"
        )
        st.markdown(
            "[![Documentation](https://img.shields.io/badge/Docs-grey?logo=readthedocs&style=plastic)]"
            "(https://memoryfm.readthedocs.io/en/stable/)"
        )
    pg.run()
