from __future__ import annotations
from pathlib import Path
import streamlit as st
from memoryfm import ScrobbleLog
from datetime import datetime


PADDING = """
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 3rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    </style>
    """

PATH = Path("data/lazulinoother")

def set_session_data(
    username: str,
    max_length: int = 10,
    from_date: str | None = None,
    to_date: str | None = None,
    **kwargs,
) -> None:
    if username is not None:
        st.session_state["username"] = username
        st.session_state["max"] = max_length
        st.session_state["sc_log"] = ScrobbleLog.from_parquet(
            meta_file=PATH / f"{username}-meta.json",
            df_file=PATH / f"{username}-df.parquet",
            start=from_date, end=to_date, **kwargs
        )
        if from_date is None:
            st.session_state["from"] = datetime.fromisoformat(
                st.session_state["sc_log"].meta["date_range"]["start"]
            )
        else:
            st.session_state["from"] = from_date
        if to_date is None:
            st.session_state["to"] = datetime.fromisoformat(
                st.session_state["sc_log"].meta["date_range"]["end"]
            )
        else:
            st.session_state["to"] = to_date
        if from_date is None and to_date is None:
            st.session_state["date_range"] = "All Time"
        else:
            st.session_state["date_range"] = (
                f"{st.session_state['from'].strftime('%d %b %Y')} to"
                f" {st.session_state['to'].strftime('%d %b %Y')}"
            )
        st.session_state["meta"] = st.session_state["sc_log"].meta
    else:
        raise RuntimeError
