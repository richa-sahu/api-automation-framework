import pytest
import allure
from src.auth import AuthClient
from src.booking import BookingClient

BASE_URL = "https://restful-booker.herokuapp.com"
USERNAME = "admin"
PASSWORD = "password123"

@pytest.fixture(scope="session")
def auth_client():
    return AuthClient(BASE_URL)

@pytest.fixture(scope="session")
def token(auth_client):
    response = auth_client.create_token(USERNAME, PASSWORD)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data, f"Token not found in response: {data}"
    return data["token"]

@pytest.fixture(scope="session")
def booking_client(token):
    return BookingClient(BASE_URL, token=token)

@pytest.fixture(scope="function")
def created_booking(booking_client):
    """Creates a booking before the test and cleans it up after."""
    from helpers.helpers import generate_booking_payload
    payload = generate_booking_payload()
    response = booking_client.create_booking(payload)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]

    yield booking_id, payload

    # Teardown — delete after test
    booking_client.delete_booking(booking_id)