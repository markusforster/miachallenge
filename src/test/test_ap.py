from fastapi.testclient import TestClient
import sys

from api import app

client = TestClient(app)

def test_version():
    response = client.get("/")
    assert response.status_code == 200

def test_known_item():
    response = client.post(
            "/predict_icd",
            json={"payload":"Arterienriss"}
            )
    assert response.status_code == 200
    assert response.json() == "I77.2"

def test_unknown_item():
    response = client.post(
            "/predict_icd",
            json={"payload":"Karzinom des Zungengrundes"}
            )
    assert response.status_code == 200
    assert response.json() == "C01"


