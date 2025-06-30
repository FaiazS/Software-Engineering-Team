import pytest
from fastapi.testclient import TestClient
from user_service import the_app, default_users
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str

@pytest.fixture
def client():
    yield TestClient(the_app)

def test_register(client):
    response = client.post("/api/users/register", json={"username": "testuser", "email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert response.json() == {"msg": "User registered successfully"}
    assert len(default_users) == 1

def test_register_duplicate_username(client):
    client.post("/api/users/register", json={"username": "testuser", "email": "test@example.com", "password": "password"})
    response = client.post("/api/users/register", json={"username": "testuser", "email": "test@example.com", "password": "password"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Username already exists"}

def test_login_success(client):
    client.post("/api/users/register", json={"username": "testuser", "email": "test@example.com", "password": "password"})
    response = client.post("/api/users/login", json={"username": "testuser", "password": "password"})
    assert response.status_code == 200
    assert "token-" in response.json()["token"]

def test_login_invalid_credentials(client):
    response = client.post("/api/users/login", json={"username": "nonexistent", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}