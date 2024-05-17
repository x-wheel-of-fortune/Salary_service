# Test successful login
def test_login_success(client, test_db):
    # Create a user first
    client.post(
        "/user",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword",
            "salary": 50000,
            "promotion_date": "2024-05-17T00:00:00"
        },
    )

    # Attempt login with correct credentials
    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "securepassword"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


# Test login with incorrect password
def test_login_incorrect_password(client, test_db):
    # Create a user first
    client.post(
        "/user",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword",
            "salary": 50000,
            "promotion_date": "2024-05-17T00:00:00"
        },
    )

    # Attempt login with incorrect password
    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert "Incorrect username or password" in response.text


# Test login with non-existing username
def test_login_non_existing_username(client, test_db):
    # Attempt login with a username that doesn't exist
    response = client.post(
        "/auth/login",
        json={"username": "nonexistinguser", "password": "somepassword"},
    )
    assert response.status_code == 401
    assert "Incorrect username or password" in response.text


# Test login with missing credentials
def test_login_missing_credentials(client, test_db):
    # Attempt login with missing credentials
    response = client.post("/auth/login")
    assert response.status_code == 422
    assert "missing" in response.text

# Add more tests for other failure scenarios, validation errors, etc.
