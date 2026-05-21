# Text Analysis Backend

## Tech Stack

- FastAPI
- SQLite
- SQLAlchemy
- Python

## Features

- Batch Processing APIs
- Multi Tenant Support
- Partial Failure Handling
- Status Tracking
- Results & Failures Endpoints

## Run Project

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## API Endpoints

POST /batches

GET /batches/{batch_id}

GET /batches/{batch_id}/results

GET /batches/{batch_id}/failures

## Sample Request

POST /batches

Header:
x-tenant-id: tenant1

Body:

[
  "hello world",
  "python backend",
  "fastapi project"
]

## Run Tests

pytest

## Design Notes

- FastAPI-based backend for batch text processing
- Multi-tenant isolation using request headers
- Partial failure handling supported
- SQLite used for lightweight persistence
- Current implementation focuses on core workflow and API behavior