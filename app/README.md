```bash
curl -X POST "http://localhost:8000/user" \
     -H "Content-Type: application/json" \
     -d '{
           "username": "newuser",
           "email": "newuser@example.com",
           "password": "securepassword",
           "salary": 50000,
           "promotion_date": "2024-05-17T00:00:00"
         }'

```