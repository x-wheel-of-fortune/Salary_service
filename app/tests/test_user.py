import pytest

# Test successful user creation
def test_create_user_success(client, test_db):
    response = client.post(
        "/user",
        json={
            "username": "testuser",
            "password": "securepassword",
            "salary": 50000,
            "promotion_date": "2024-05-17T00:00:00"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"

# Test creating user with existing username
def test_create_user_existing_username(client, test_db):
    # Create a user with the same username first
    client.post(
        "/user",
        json={
            "username": "testuser",
            "password": "existingpassword",
            "salary": 60000,
            "promotion_date": "2024-05-17T00:00:00"
        },
    )
    # Attempt to create a new user with the same username
    response = client.post(
        "/user",
        json={
            "username": "testuser",
            "password": "securepassword",
            "salary": 50000,
            "promotion_date": "2024-05-17T00:00:00"
        },
    )
    assert response.status_code == 400
    assert "Username already exists" in response.text


# Test creating user with invalid data
def test_create_user_invalid_data(client, test_db):
    # Attempt to create a user with missing required fields
    response = client.post(
        "/user",
        json={
            "password": "securepassword",
            "salary": 50000,
            "promotion_date": "2024-05-17T00:00:00"
        },
    )
    assert response.status_code == 422
    assert "missing" in response.text

# Add more tests for other failure scenarios, validation errors, etc.
