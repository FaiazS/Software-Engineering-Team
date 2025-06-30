import pytest
from fastapi.testclient import TestClient
from integration_service import the_app

@pytest.fixture
def client():
    yield TestClient(the_app)

def test_share_video_youtube(client):
    response = client.post("/api/integration/share", json={"video_id": 1