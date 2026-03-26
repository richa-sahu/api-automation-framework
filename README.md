# API Automation Framework

![CI](https://github.com/richa-sahu/api-automation-framework/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Pytest](https://img.shields.io/badge/pytest-7.4.0-green)
![Allure](https://img.shields.io/badge/allure-2.13.2-orange)
![Docker](https://img.shields.io/badge/docker-enabled-blue)

A production-grade REST API test automation framework built with **Pytest**, **Requests**, **Allure**, **Docker**, and **GitHub Actions CI/CD** — targeting the [Restful Booker API](https://restful-booker.herokuapp.com).

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Pytest | Test runner |
| Requests | HTTP client |
| Allure | Test reporting |
| Faker | Dynamic test data generation |
| Docker | Containerized test execution |
| GitHub Actions | CI/CD pipeline |

---

## Project Structure
```
api-automation-framework/
├── src/
│   ├── base_client.py      # Base HTTP client with Allure attachments
│   ├── auth.py             # Authentication client
│   └── booking.py          # Booking API client
├── tests/
│   ├── conftest.py         # Fixtures and session setup
│   ├── test_auth.py        # Auth tests (valid, invalid, missing)
│   └── test_booking.py     # Booking CRUD + negative + parametrized
├── helpers/
│   └── helpers.py          # Test data generators using Faker
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions pipeline
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
└── requirements.txt
```

---

## Test Coverage

| Category | Tests |
|----------|-------|
| Auth — valid credentials | ✅ |
| Auth — invalid credentials | ✅ |
| Auth — missing credentials | ✅ |
| Get all bookings | ✅ |
| Create booking | ✅ |
| Get booking by ID | ✅ |
| Update booking (PUT) | ✅ |
| Partial update (PATCH) | ✅ |
| Delete booking | ✅ |
| Get non-existent booking (404) | ✅ |
| Update without auth (403) | ✅ |
| Delete without auth (403) | ✅ |
| Filter by name (parametrized) | ✅ |
| Varied pricing (parametrized) | ✅ |

---

## Running Locally

**1. Clone and set up virtual environment:**
```bash
git clone https://github.com/richa-sahu/api-automation-framework.git
cd api-automation-framework
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**2. Create `.env` file:**
```
BASE_URL=https://restful-booker.herokuapp.com
BOOKING_USERNAME=admin
BOOKING_PASSWORD=password123
```

**3. Run all tests:**
```bash
pytest
```

**4. Run by marker:**
```bash
pytest -m smoke
pytest -m regression
pytest -m negative
```

**5. Generate Allure report:**
```bash
allure serve reports/allure-results
```

---

## Running with Docker
```bash
docker-compose up --build
```

---

## CI/CD

Every push to `main` triggers the GitHub Actions pipeline which:
- Installs dependencies on Ubuntu latest
- Runs the full test suite
- Uploads Allure results as a downloadable artifact

---

## Author

**Richa Sahu** — Senior SDET  
[LinkedIn](https://linkedin.com/in/richasahu27) | [GitHub](https://github.com/richa-sahu)


