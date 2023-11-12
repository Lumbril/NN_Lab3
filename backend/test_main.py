from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_incorrect_file():
    file_path = "labels.txt"

    with open(file_path, "rb") as file:
        response = client.post("/api/model", files={"file": ("labels.txt", file)})

    assert response.status_code == 400
    assert response.json() == {"detail": "The file must have an extension .jpg or .png"}


def test_predict1():
    file_path = "sombrero.jpg"

    with open(file_path, "rb") as file:
        response = client.post("/api/model", files={"file": ("sombrero.jpg", file)})

    assert response.status_code == 200
    assert response.json()["target_name"] == 'sombrero'
