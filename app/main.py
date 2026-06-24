from fastapi import FastAPI

from app.api.v1.datasets import router as dataset_router
from app.api.v1.health import router as health_router
from app.core.config import settings

# Create database tables
from app.core.database import Base, engine
from app.models.dataset import Dataset

app = FastAPI(
    title=settings.APP_NAME,
)

# Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Self Healing Data Pipeline API"}


app.include_router(health_router, prefix="/api/v1", tags=["health"])

app.include_router(dataset_router, prefix="/api/v1", tags=["Datasets"])
