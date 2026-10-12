from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "ai-docker-lab",
    }


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "AI Engineer Docker Lab",
        "docs": "/docs",
        "version": "1.0.0",
    }


def test_unknown_route():
    response = client.get("/unknown")

    assert response.status_code == 404
