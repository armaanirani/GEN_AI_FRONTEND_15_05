import streamlit as st
from utils.config import app_config, env_config
from utils.logger import logger

st.set_page_config(
    page_title="Test App",
    page_icon="🎯",
    layout="centered",
)

st.title("Template App for Gen AI Applications")

col1, col2 = st.columns(2)

if col1.button("Check Server Health"):
    st.success("Server is healthy!")


if col2.button("List LLMs"):
    st.success("Server is healthy!!")