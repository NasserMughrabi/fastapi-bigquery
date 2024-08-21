from fastapi.testclient import TestClient
from app.main import app
from app.api.models.item import Item

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"id": "1", "name": "Item 1"})
    assert response.status_code == 200
    assert response.json() == {"message": "Item successfully inserted"}

def test_read_item():
    # Assuming the item was created before this test
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": "1", "name": "Item 1"}
