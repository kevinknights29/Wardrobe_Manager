from __future__ import annotations

import datetime

import streamlit as st

from src.utils import common

logger = common.create_logger(__name__)

APP_PAGE_TITLE = common.config()["app"]["page_title"]
APP_PAGE_ICON = common.config()["app"]["page_icon"]
APP_TITLE = common.config()["app"]["title"]
APP_ONBOARDING = common.config()["app"]["onboarding"]
CAMERA_INSTRUCTION = common.config()["app"]["camera_instruction"]
SELECT_INSTRUCTION = common.config()["app"]["select"]["instruction"]
SELECT_OPTIONS = common.config()["app"]["select"]["options"]
DATE_INSTUCTION = common.config()["app"]["date_instruction"]
SUBMIT_INSTUCTION = common.config()["app"]["submit_instruction"]

# Set Page Configuration
st.set_page_config(
    page_title=APP_PAGE_TITLE,
    page_icon=APP_PAGE_ICON,
)

# Set the page title and onboarding text
st.title(APP_TITLE)
st.markdown("\n".join(APP_ONBOARDING))
st.divider()

# Take a picture of the item
picture = st.camera_input(CAMERA_INSTRUCTION)
if picture:
    st.image(picture)

# Label the item
st.selectbox(SELECT_INSTRUCTION, SELECT_OPTIONS)

# Log usage of the item
st.date_input(DATE_INSTUCTION, datetime.date.today())

# Submit item
st.button(SUBMIT_INSTUCTION)
