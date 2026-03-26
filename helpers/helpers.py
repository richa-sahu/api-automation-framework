from faker import Faker

fake = Faker()

def generate_booking_payload(
    firstname=None,
    lastname=None,
    total_price=None,
    deposit_paid=None,
    checkin="2025-01-01",
    checkout="2025-01-07",
    additional_needs="Breakfast"
):
    return {
        "firstname": firstname or fake.first_name(),
        "lastname": lastname or fake.last_name(),
        "totalprice": total_price if total_price is not None else fake.random_int(min=100, max=1000),
        "depositpaid": deposit_paid if deposit_paid is not None else True,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additional_needs
    }