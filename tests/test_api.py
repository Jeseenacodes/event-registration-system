from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_get_events():
    response = client.get("/api/events")

    assert response.status_code == 200

    data = response.json()

    assert len(data) >= 1
    assert "event_id" in data[0]
    assert "name" in data[0]
    assert "event_date" in data[0]
    assert "location" in data[0]


def test_get_event_registrations():
    response = client.get("/api/events/1/registrations")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_duplicate_registration_is_rejected():

    registration = {
        "first_name": "Jordan",
        "last_name": "Lee",
        "email": "jordan@example.com",
        "organization": "Community AI",
        "event_id": 1
    }

    response = client.post(
        "/api/registrations",
        json=registration
    )

    data = response.json()

    assert "error" in data
    assert data["error"] == "You are already registered for this event."