from fastapi import FastAPI
import os

APP_ENV = os.getenv("APP_ENV", "development")

app = FastAPI(
    title="AI Engineer Docker Lab",
    version="1.0.0",
    description="A minimal API for learning AI service deployment.",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "ai-docker-lab",
    }


@app.get("/")
def root():
    return {
        "message": "AI Engineer Docker Lab",
        "docs": "/docs",
        "version": "1.0.0",
        "environment": APP_ENV,
    }
