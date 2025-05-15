import requests 
from utils.config import app_config
from utils.logger import logger

base_url = app_config["api_url"]

def test_health():
    """
    Test the health of the server.
    """
    health_api_endpoint = f"{base_url}/health"
    logger.info(f"Sending GET request to {health_api_endpoint}")
    
    try:
        response = requests.get(health_api_endpoint)
        response.raise_for_status()  # Raise an error for bad responses
        logger.info("Health check successful.")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Health check failed: {e}")
        return {"error": "Unable to connct to the server health endpoint."}