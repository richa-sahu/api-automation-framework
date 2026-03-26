import requests
import logging
import allure
import json

logger = logging.getLogger(__name__)

class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def _attach_to_allure(self, response: requests.Response):
        """Attach request and response details to Allure report."""
        # Request details
        request = response.request
        request_body = ""
        if request.body:
            try:
                request_body = json.dumps(json.loads(request.body), indent=2)
            except Exception:
                request_body = str(request.body)

        allure.attach(
            f"URL: {request.url}\nMethod: {request.method}\nHeaders: {dict(request.headers)}\nBody:\n{request_body}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

        # Response details
        response_body = ""
        try:
            response_body = json.dumps(response.json(), indent=2)
        except Exception:
            response_body = response.text

        allure.attach(
            f"Status Code: {response.status_code}\nBody:\n{response_body}",
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        response = self.session.get(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        self._attach_to_allure(response)
        return response

    def post(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        response = self.session.post(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        self._attach_to_allure(response)
        return response

    def put(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url}")
        response = self.session.put(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        self._attach_to_allure(response)
        return response

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = self.session.delete(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        self._attach_to_allure(response)
        return response

    def patch(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH {url}")
        response = self.session.patch(url, **kwargs)
        logger.info(f"Response: {response.status_code}")
        self._attach_to_allure(response)
        return response