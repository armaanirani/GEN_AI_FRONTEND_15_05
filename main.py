import streamlit as st
from utils.config import app_config, env_config
from utils.logger import logger
from services.check_server_health import test_health
from services.get_llms_list import get_llms_list

st.set_page_config(
    page_title="Test App",
    page_icon="🎯",
    layout="centered",
)

st.title("Template App for Gen AI Applications")

col1, col2 = st.columns(2)

if col1.button("Check Server Health"):
    logger.info("Checking server health...")
    result = test_health()
    logger.info(f"Server health check result: {result}")
    st.json(result)


if col2.button("List LLMs"):
    logger.info("Fetching LLMs list...")
    list_of_llms = get_llms_list()
    logger.info(f"LLMs list retrieval result: {list_of_llms}")
    st.json(list_of_llms)