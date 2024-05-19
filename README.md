# FastAPI User Management and Salary Service

This project is a RESTful API service built with FastAPI for managing user accounts and viewing salary information. It includes authentication mechanisms to ensure that only authorized users can access sensitive salary data.

## Features

- User Authentication
- Retrieve Current Salary
- Retrieve Date of Next Salary Increase
- Secure Endpoints with JWT Token

## Getting Started

### Prerequisites

- GNU Make
- Docker and Docker Compose
- Python 3.12 with Poetry

### Installation

1. **Clone the repository**
2. **Set up the environment variables:**

   Set variables in `.env` file if needed

   ```env
   POSTGRES_DB=yourdbname
   POSTGRES_USER=yourdbuser
   POSTGRES_PASSWORD=yourdbpassword
   POSTGRES_SERVER=localhost
   ```

3. **Install dependencies:**

   ```sh
   poetry install
   ```

### Running the Application

1. **Build and start the Docker containers:**

   ```sh
   make up
   ```

2. **Access the API:**

   The API will be available at `http://localhost:8000`

## Endpoints

| Endpoint                    | Description                 |
|-----------------------------|-----------------------------|
| `POST /user`                | Create new user             |
| `POST /login`               | Get access token for a user |
| `GET /salary`               | Get salary information      |

### User Registration

- **URL:** `/user`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "username": "testuser",
      "email": "testuser@example.com",
      "password": "securepassword",
      "salary": 50000,
      "promotion_date": "2024-05-17T00:00:00"
  }
  ```
- **Response:** `201 Created`

### User Authentication

- **URL:** `/login`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "username": "testuser",
      "password": "securepassword"
  }
  ```
- **Response:**
  ```json
  {
      "access_token": "access_token",
      "token_type": "bearer"
  }
  ```

### Retrieve Salary Information

- **URL:** `/salary`
- **Method:** `GET`
- **Headers:**
  ```http
  Authorization: Bearer access_token
  ```
- **Response:**
  ```json
  {
      "salary": 50000,
      "promotion_date": "2024-05-17T00:00:00"
  }
  ```
### Template requests for quick copy and paste
```sh
curl -X POST "http://localhost:8000/user"      -H "Content-Type: application/json"      -d '{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "securepassword",
    "salary": 50000,
    "promotion_date": "2024-05-17T00:00:00"
}'
```
```sh
curl -X POST "http://localhost:8000/auth/login"      -H "Content-Type: application/json"      -d '{
    "username": "testuser",
    "password": "securepassword"
}'
```
```sh
curl -X GET "http://localhost:8000/salary" \
     -H "Authorization: Bearer <access_token>"
```
  
## Makefile

You can find more useful commands if you run
```sh
make help
```

