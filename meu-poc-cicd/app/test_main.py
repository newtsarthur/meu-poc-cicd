from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_rota_principal_retorna_versao():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["versao"] == "1.0"


def test_health_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
