import streamlit as st
from utils.config import app_config, env_config
from utils.logger import logger

st.set_page_config(
    page_title="Test App",
    page_icon="🎯",
    layout="centered",
)

st.title("Template App for Gen AI Applications")