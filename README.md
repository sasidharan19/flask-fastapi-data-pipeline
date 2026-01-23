## Customer Data Pipeline

### Run
docker-compose up -d

### Test Flask
curl http://localhost:5000/api/customers?page=1&limit=5

### Ingest
curl -X POST http://localhost:8000/api/ingest

### Query
curl http://localhost:8000/api/customers?page=1&limit=5
