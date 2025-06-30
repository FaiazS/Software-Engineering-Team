import pytest
from fastapi.testclient import TestClient
from notification_service import notification_service

@pytest.fixture
def client():
    yield TestClient(notification_service)

def test_send_notification(client):
    response = client.post("/api/notifications", json={"user_id": "testuser", "message": "Hello!"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Notification sent"}