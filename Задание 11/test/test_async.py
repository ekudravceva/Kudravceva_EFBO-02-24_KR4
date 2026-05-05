import pytest
from httpx import AsyncClient, ASGITransport
from faker import Faker
from app.main import app, db

fake = Faker()

@pytest.mark.asyncio
class TestAsyncCreateUser:
    async def test_create_user_success(self):
        db.clear()
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            response = await ac.post("/users", json={
                "username": fake.user_name(),
                "age": fake.random_int(min=19, max=80)
            })
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["username"] is not None
        assert data["age"] > 18

    async def test_create_user_boundary_age(self):
        db.clear()
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            response = await ac.post("/users", json={
                "username": fake.user_name(),
                "age": 19
            })
        assert response.status_code == 201

@pytest.mark.asyncio
class TestAsyncGetUser:
    async def test_get_existing_user(self):
        db.clear()
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            create_resp = await ac.post("/users", json={
                "username": fake.user_name(),
                "age": fake.random_int(min=19, max=80)
            })
            user_id = create_resp.json()["id"]
            get_resp = await ac.get(f"/users/{user_id}")
        assert get_resp.status_code == 200
        assert get_resp.json()["id"] == user_id

    async def test_get_nonexistent_user(self):
        db.clear()
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            response = await ac.get("/users/99999")
        assert response.status_code == 404

@pytest.mark.asyncio
class TestAsyncDeleteUser:
    async def test_delete_existing_user(self):
        db.clear()
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            create_resp = await ac.post("/users", json={
                "username": fake.user_name(),
                "age": fake.random_int(min=19, max=80)
            })
            user_id = create_resp.json()["id"]
            delete_resp = await ac.delete(f"/users/{user_id}")
        assert delete_resp.status_code == 204

    async def test_double_delete_user(self):
        db.clear()
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            create_resp = await ac.post("/users", json={
                "username": fake.user_name(),
                "age": fake.random_int(min=19, max=80)
            })
            user_id = create_resp.json()["id"]
            await ac.delete(f"/users/{user_id}")
            second_delete = await ac.delete(f"/users/{user_id}")
        assert second_delete.status_code == 404