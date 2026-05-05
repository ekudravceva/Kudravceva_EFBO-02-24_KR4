from fastapi.testclient import TestClient
from app.main import app, db

client = TestClient(app)

class TestCreateUser:
    def test_create_user_success(self):
        db.clear()
        response = client.post("/users", json={"username": "test", "age": 25})
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == "test"
        assert data["age"] == 25
        assert "id" in data

    def test_create_user_invalid_data(self):
        db.clear()
        response = client.post("/users", json={"username": 123, "age": "not_int"})
        assert response.status_code == 422

class TestGetUser:
    def test_get_existing_user(self):
        db.clear()
        response = client.post("/users", json={"username": "test", "age": 25})
        user_id = response.json()["id"]
        response = client.get(f"/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["username"] == "test"

    def test_get_nonexistent_user(self):
        db.clear()
        response = client.get("/users/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "User not found"

class TestDeleteUser:
    def test_delete_existing_user(self):
        db.clear()
        response = client.post("/users", json={"username": "test", "age": 25})
        user_id = response.json()["id"]
        response = client.delete(f"/users/{user_id}")
        assert response.status_code == 204

    def test_delete_nonexistent_user(self):
        db.clear()
        response = client.delete("/users/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "User not found"

    def test_double_delete_user(self):
        db.clear()
        response = client.post("/users", json={"username": "test", "age": 25})
        user_id = response.json()["id"]
        client.delete(f"/users/{user_id}")
        response = client.delete(f"/users/{user_id}")
        assert response.status_code == 404