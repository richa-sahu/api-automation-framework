import allure
from src.base_client import BaseClient

class BookingClient(BaseClient):
    def __init__(self, base_url: str, token: str = None):
        super().__init__(base_url)
        if token:
            self.session.cookies.set("token", token)

    @allure.step("Get all booking IDs")
    def get_all_bookings(self, params: dict = None):
        return self.get("/booking", params=params)

    @allure.step("Get booking by ID: {booking_id}")
    def get_booking(self, booking_id: int):
        return self.get(f"/booking/{booking_id}")

    @allure.step("Create new booking")
    def create_booking(self, payload: dict):
        return self.post("/booking", json=payload)

    @allure.step("Update booking ID: {booking_id}")
    def update_booking(self, booking_id: int, payload: dict):
        return self.put(f"/booking/{booking_id}", json=payload)

    @allure.step("Partial update booking ID: {booking_id}")
    def partial_update_booking(self, booking_id: int, payload: dict):
        return self.patch(f"/booking/{booking_id}", json=payload)

    @allure.step("Delete booking ID: {booking_id}")
    def delete_booking(self, booking_id: int):
        return self.delete(f"/booking/{booking_id}")