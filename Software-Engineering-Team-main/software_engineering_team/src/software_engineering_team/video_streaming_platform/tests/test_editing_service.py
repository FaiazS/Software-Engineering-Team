import pytest
from fastapi.testclient import TestClient
from editing_service import the_app

@pytest.fixture
def client():
    yield TestClient(the_app)

def test_edit_video_trim(client):
    response = client.post("/api/videos/1/edit", json={"video_id": 1