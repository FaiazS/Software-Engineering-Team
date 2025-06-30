import pytest
from fastapi.testclient import TestClient
from video_service import the_app, videos
from pydantic import BaseModel

class Video(BaseModel):
    id: int
    title: str
    content: str
    user_id: str

@pytest.fixture
def client():
    yield TestClient(the_app)

def test_upload_video(client):
    response = client.post("/api/videos/upload", json={"id": 1