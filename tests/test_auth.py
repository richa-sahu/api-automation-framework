import allure
import pytest

@allure.feature("Authentication")
class TestAuth:

    @allure.story("Valid credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_create_token_success(self, auth_client):
        response = auth_client.create_token("admin", "password123")
        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        assert len(data["token"]) > 0

    @allure.story("Invalid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    def test_create_token_invalid_credentials(self, auth_client):
        response = auth_client.create_token("wronguser", "wrongpass")
        assert response.status_code == 200
        data = response.json()
        # RestfulBooker returns {"reason": "Bad credentials"} on failure
        assert "reason" in data or "token" not in data

    @allure.story("Missing credentials")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_create_token_missing_password(self, auth_client):
        response = auth_client.create_token("admin", "")
        assert response.status_code == 200
        data = response.json()
        assert "reason" in data or "token" not in data