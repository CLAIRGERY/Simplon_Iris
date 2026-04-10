from fastapi.testclient import TestClient
from app.Iris_Api import app

client = TestClient(app)

def test_health_check():
    """Vérifie que la route GET / fonctionne"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict_valid_data():
    """Vérifie une prédiction avec des données correctes"""
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], list)

def test_predict_invalid_data():
    """Vérifie que l'API rejette les mauvaises données (ex: texte)"""
    payload = {"features": ["cinq", 3.5, 1.4, "erreur"]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422 # Erreur de validation Pydantic