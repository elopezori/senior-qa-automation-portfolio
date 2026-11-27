
from jsonschema import validate, FormatChecker

from schemas.user_schema import USER_SCHEMA


def test_get_user_returns_successful_response(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200

    user = response.json()

    validate(
        instance=user,
        schema=USER_SCHEMA,
        format_checker=FormatChecker()
    )

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["email"] == "Sincere@april.biz"


def test_create_user_returns_created_user(api_client):
    payload = {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }

    response = api_client.post("/users", json=payload)

    assert response.status_code == 201

    created_user = response.json()

    assert created_user["name"] == payload["name"]
    assert created_user["username"] == payload["username"]
    assert created_user["email"] == payload["email"]
    assert "id" in created_user