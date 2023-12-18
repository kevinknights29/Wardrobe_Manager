from __future__ import annotations

import datetime

import streamlit as st

from src.utils import common

logger = common.create_logger(__name__)

# App Configuration
APP_PAGE_TITLE = common.config()["app"]["page_title"]
APP_PAGE_ICON = common.config()["app"]["page_icon"]

# Home Page Configuration
HOME_TITLE = common.config()["home"]["title"]
HOME_ONBOARDING = common.config()["home"]["onboarding"]
CAMERA_INSTRUCTION = common.config()["home"]["camera_instruction"]
SELECT_INSTRUCTION = common.config()["home"]["select"]["instruction"]
SELECT_OPTIONS = common.config()["home"]["select"]["options"]
DATE_INSTUCTION = common.config()["home"]["date_instruction"]
SUBMIT_INSTUCTION = common.config()["home"]["submit_instruction"]


def home() -> None:
    """Home page for the app."""
    # Set the page title and onboarding text
    st.title(HOME_TITLE)
    st.markdown("\n".join(HOME_ONBOARDING))
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


if __name__ == "__main__":
    logger.info("Starting Streamlit App")

    # Set App Configuration
    logger.info("Setting App Configuration")
    st.set_page_config(
        page_title=APP_PAGE_TITLE,
        page_icon=APP_PAGE_ICON,
    )

    # Display Home Page
    logger.info("Displaying Home Page")
    home()
