import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_batch():

    response = client.post(
        "/batches",
        headers={
            "x-tenant-id": "tenant1",
            "Idempotency-Key": "abc123"
        },
        json=[
            "hello",
            "world"
        ]
    )

    assert response.status_code == 200
    assert "batch_id" in response.json()


def test_batch_status():

    response = client.get("/batches/1")

    assert response.status_code == 200


def test_results_endpoint():

    response = client.get("/batches/1/results")

    assert response.status_code == 200


def test_failures_endpoint():

    response = client.get("/batches/1/failures")

    assert response.status_code == 200