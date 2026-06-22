from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import dataset
from app.repositories.dataset_repository import DatasetRepository


from fastapi import UploadFile
from fastapi import File

from app.services.csv_service import CSVService

from app.services.schema_validator import SchemaValidator

from app.services.healing_service import HealingService

from app.repositories.healing_log_repository import (
    HealingLogRepository
)

from app.services.pipeline_service import PipelineService

router = APIRouter()


@router.post("/datasets/test")
def create_dataset(
    db: Session = Depends(get_db)
):

    dataset = DatasetRepository.create(
        db=db,
        filename="sample.csv"
    )

    return {
        "id": str(dataset.id),
        "filename": dataset.filename
    }


@router.post("/datasets/upload")
def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    return PipelineService.process_dataset(
        file=file,
        db=db
    )


@router.get("/healing-logs")
def get_healing_logs(
    db: Session = Depends(get_db)
):

    logs = HealingLogRepository.get_all(db)

    return logs