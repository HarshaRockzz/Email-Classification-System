import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_classify_email():
    response = client.post("/classify", json={
        "email_body": "Subject: Issue\nHello, my name is John Doe, contact me at john@example.com."
    })
    assert response.status_code == 200
    assert "category_of_the_email" in response.json()
    assert "list_of_masked_entities" in response.json()