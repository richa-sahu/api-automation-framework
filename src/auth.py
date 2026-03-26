import allure
from src.base_client import BaseClient

class AuthClient(BaseClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    @allure.step("Generate auth token with username={username}")
    def create_token(self, username: str, password: str) -> dict:
        payload = {"username": username, "password": password}
        response = self.post("/auth", json=payload)
        return response