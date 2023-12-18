from __future__ import annotations

import streamlit as st

from src.utils import common

logger = common.create_logger(__name__)

TRACKER_TITLE = common.config()["tracker"]["title"]

st.title(TRACKER_TITLE)
