import allure
import pytest
import os
from dotenv import load_dotenv
from helpers.helpers import generate_booking_payload

load_dotenv()
BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")


@allure.feature("Booking")
class TestBookingPositive:

    @allure.story("Get all bookings")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_all_bookings(self, booking_client):
        response = booking_client.get_all_bookings()
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

    @allure.story("Create booking")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_create_booking(self, booking_client):
        payload = generate_booking_payload()
        response = booking_client.create_booking(payload)
        assert response.status_code == 200
        data = response.json()
        assert "bookingid" in data
        assert data["booking"]["firstname"] == payload["firstname"]
        assert data["booking"]["lastname"] == payload["lastname"]

    @allure.story("Get booking by ID")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_get_booking_by_id(self, booking_client, created_booking):
        booking_id, original_payload = created_booking
        response = booking_client.get_booking(booking_id)
        assert response.status_code == 200
        data = response.json()
        assert data["firstname"] == original_payload["firstname"]
        assert data["totalprice"] == original_payload["totalprice"]

    @allure.story("Update booking")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_update_booking(self, booking_client, created_booking):
        booking_id, _ = created_booking
        updated_payload = generate_booking_payload(
            firstname="UpdatedFirst",
            lastname="UpdatedLast"
        )
        response = booking_client.update_booking(booking_id, updated_payload)
        assert response.status_code == 200
        data = response.json()
        assert data["firstname"] == "UpdatedFirst"
        assert data["lastname"] == "UpdatedLast"

    @allure.story("Partial update booking")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_partial_update_booking(self, booking_client, created_booking):
        booking_id, _ = created_booking
        response = booking_client.partial_update_booking(
            booking_id,
            {"firstname": "PatchedName"}
        )
        assert response.status_code == 200
        assert response.json()["firstname"] == "PatchedName"

    @allure.story("Delete booking")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_delete_booking(self, booking_client):
        payload = generate_booking_payload()
        create_resp = booking_client.create_booking(payload)
        booking_id = create_resp.json()["bookingid"]

        delete_resp = booking_client.delete_booking(booking_id)
        assert delete_resp.status_code == 201

        get_resp = booking_client.get_booking(booking_id)
        assert get_resp.status_code == 404


@allure.feature("Booking")
class TestBookingNegative:

    @allure.story("Get non-existent booking")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_get_booking_invalid_id(self, booking_client):
        response = booking_client.get_booking(999999999)
        assert response.status_code == 404

    @allure.story("Update without auth")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    def test_update_booking_no_auth(self, created_booking):
        from src.booking import BookingClient
        unauthenticated_client = BookingClient(BASE_URL)
        booking_id, payload = created_booking
        response = unauthenticated_client.update_booking(booking_id, payload)
        assert response.status_code == 403

    @allure.story("Delete without auth")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    def test_delete_booking_no_auth(self, created_booking):
        from src.booking import BookingClient
        unauthenticated_client = BookingClient(BASE_URL)
        booking_id, _ = created_booking
        response = unauthenticated_client.delete_booking(booking_id)
        assert response.status_code == 403


@allure.feature("Booking")
class TestBookingParametrized:

    @allure.story("Filter bookings by name")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.parametrize("firstname,lastname", [
        ("John", "Smith"),
        ("Jane", "Doe"),
        ("Alice", "Brown"),
    ])
    def test_get_bookings_by_name_filter(self, booking_client, firstname, lastname):
        payload = generate_booking_payload(firstname=firstname, lastname=lastname)
        booking_client.create_booking(payload)

        response = booking_client.get_all_bookings(
            params={"firstname": firstname, "lastname": lastname}
        )
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @allure.story("Create booking with varied pricing")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.parametrize("price,deposit", [
        (100, True),
        (0, False),
        (9999, True),
    ])
    def test_create_booking_varied_price(self, booking_client, price, deposit):
        payload = generate_booking_payload(total_price=price, deposit_paid=deposit)
        response = booking_client.create_booking(payload)
        assert response.status_code == 200
        data = response.json()
        assert data["booking"]["totalprice"] == price
        assert data["booking"]["depositpaid"] == deposit