import requests
from utils.config import app_config, env_config
from utils.logger import logger

base_url = app_config["api_url"]
app_api_key = env_config.APP_API_KEY

headers = {
    "accept": "application/json",
    "api-key": app_api_key
}

def get_llms_list():
    """
    Get the list of available LLMs from the server.
    """
    llms_api_endpoint = f"{base_url}/llm/llm_options"
    logger.info(f"Sending GET request to {llms_api_endpoint}")
    
    try:
        response = requests.get(url=llms_api_endpoint, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        logger.info("LLMs list retrieval successful.")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logger.error(f"LLMs list retrieval failed: {e}")
        return {"error": "Unable to connect to the server LLMs endpoint."}