# AI Engineer Docker Lab

A minimal FastAPI service packaged with Docker Compose. This project demonstrates containerized API development, HTTP health checks, and automated testing.

## Features

- FastAPI REST API
- Health check endpoint
- Interactive API documentation
- Docker image build and container execution
- Automated API tests with pytest

## Project Structure

```text
ai-docker-lab/
├── .dockerignore
├── Dockerfile
├── app.py
├── compose.yaml
├── requirements.txt
└── tests/
    └── test_app.py
```

## Requirements

- Docker Engine
- Docker Compose
- `curl` for optional API checks

## Run the Application

Build the image and start the service:

```bash
sudo docker compose up --build -d
```

Check the running container:

```bash
sudo docker compose ps
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Service welcome message |
| GET | `/health` | Health check |
| GET | `/docs` | Interactive API documentation |

Example health check:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "ai-docker-lab"
}
```

Open the interactive API documentation in a browser:

http://localhost:8000/docs

## Run Tests

Run the automated tests inside a temporary container:

```bash
sudo docker compose run --rm --no-deps app python -m pytest -v
```

The test suite checks the health endpoint, root endpoint, and unknown-route behavior.

## View Logs

```bash
sudo docker compose logs --tail=50 app
```

## Stop the Application

```bash
sudo docker compose down
```

## Learning Objectives

- Understand Docker images, containers, and build context
- Package a Python API into a container
- Expose a containerized service through port mapping
- Run automated tests in a containerized environment
- Use Docker Compose to manage an application lifecycle

## Next Steps

- Add CI with GitHub Actions
- Improve dependency version management
- Add structured logging and request validation
- Add container health checks

