import requests
import logging

logger = logging.getLogger(__name__)

class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        response = self.session.get(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        return response

    def post(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        response = self.session.post(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        return response

    def put(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url}")
        response = self.session.put(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        return response

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = self.session.delete(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        return response

    def patch(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH {url}")
        response = self.session.patch(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        return response