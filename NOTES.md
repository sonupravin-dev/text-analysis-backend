# NOTES

## AI Assistance

AI tools were used for:
- FastAPI guidance
- Debugging
- API structure suggestions
- README and NOTES formatting

All code was reviewed and understood before submission.

- Basic API tests for batch/status/results/failures endpoints

## Overview

This implementation focuses on delivering the core backend workflow with clean API design, batch processing logic, failure handling, and multi-tenant support using FastAPI.

## What Was Implemented

- Batch processing APIs
- Batch status tracking
- Results and failures endpoints
- Multi-tenant support using request headers
- Partial failure handling
- Database persistence using SQLite
- Swagger API documentation

## What I Would Improve With More Time

- Replace SQLite with PostgreSQL
- Add Redis-backed queue management
- Implement Celery workers for asynchronous processing
- Add proper retry queues and exponential backoff
- Add authentication and authorization
- Add rate limiting and idempotency handling
- Add Docker and docker-compose support
- Improve logging and monitoring
- Add automated tests

## Simplifications / Tradeoffs

- Used SQLite instead of PostgreSQL for faster local setup and simpler execution
- Used synchronous processing instead of distributed async workers
- Simulated external API failures for demonstrating partial failure handling
- Retry handling is simplified in the current implementation

## Known Limitations

- Current implementation is not optimized for high concurrency
- SQLite is not suitable for production-scale distributed systems
- Celery and Redis integration are not implemented yet
- No authentication layer is included

## What I Am Proud Of

- Clean FastAPI project structure
- Clear separation of routes, models, tasks, and database logic
- Working batch processing flow
- Partial failure handling implementation
- Easy-to-test Swagger API setup