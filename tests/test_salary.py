import base64
import json
import time


# Test successful retrieval of user salary
def test_get_user_salary_success(client, test_db):
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

    # Login to obtain the access token
    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "securepassword"},
    )
    token = response.json()["access_token"]

    # Retrieve user salary using the access token
    response = client.get(
        "/salary",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["salary"] == 50000


# Test unauthorized access to salary endpoint without token
def test_get_user_salary_unauthorized(client, test_db):
    response = client.get("/salary")
    assert response.status_code == 401
    assert "Not authenticated" in response.text


# Test unauthorized access to salary endpoint with invalid token
def test_get_user_salary_invalid_token(client, test_db):
    response = client.get(
        "/salary",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401
    assert "Could not validate credentials" in response.text


# Test unauthorized access to salary endpoint with expired token
def test_get_user_salary_expired_token(client, test_db):
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

    # Login to obtain the access token
    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "securepassword"},
    )
    token = response.json()["access_token"]

    # Simulate an expired token by setting an expiration time in the past
    expired_token = token.split('.')
    payload = json.loads(
        base64.urlsafe_b64decode(expired_token[1] + "==").decode('utf-8'))
    payload['exp'] = int(
        time.time()) - 3600  # Set expiration time to 1 hour ago
    expired_token[1] = base64.urlsafe_b64encode(
        json.dumps(payload).encode('utf-8')).decode('utf-8').rstrip('=')
    expired_token = '.'.join(expired_token)

    # Attempt to retrieve user salary with expired token
    response = client.get(
        "/salary",
        headers={"Authorization": f"Bearer {expired_token}"}
    )
    assert response.status_code == 401
    assert "Could not validate credentials" in response.text

# Add more tests for other failure scenarios, validation errors, etc.
