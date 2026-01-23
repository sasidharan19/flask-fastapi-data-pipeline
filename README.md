## Customer Data Pipeline

This project implements a simple end-to-end data pipeline using Docker Compose.  
Customer data is served from a Flask mock API, ingested by a FastAPI service, and stored in a PostgreSQL database.

---

## Tech Stack
- Flask (Mock customer API)
- FastAPI (Data ingestion and query service)
- PostgreSQL (Data storage)
- Docker & Docker Compose

---

## How to Run

Start all services using Docker Compose:

```bash
docker-compose up -d

# Test Flask (paginated customers)
curl "http://localhost:5000/api/customers?page=1&limit=5"

# Ingest data into PostgreSQL
curl -X POST "http://localhost:8000/api/ingest"

# Get customers from FastAPI (paginated)
curl "http://localhost:8000/api/customers?page=1&limit=5"

