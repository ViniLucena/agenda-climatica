from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API funcionando"}

def test_weather_valid_city():
    response = client.get("/weather?city=London")
    assert response.status_code == 200
    json_data = response.json()
    assert "cidade" in json_data
    assert "temperatura" in json_data
    assert "descricao" in json_data

def test_weather_missing_city():
    response = client.get("/weather?city=")
    assert response.status_code == 422 # erro de validação de entrada em parametro obrigatorio


def test_weather_invalid_city():
    response = client.get("/weather?city=CityThatDoesNotExist")
    assert response.status_code == 404
    assert "detail" in response.json()