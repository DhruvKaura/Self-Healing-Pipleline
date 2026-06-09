from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.dataset_repository import DatasetRepository


from fastapi import UploadFile
from fastapi import File

from app.services.csv_service import CSVService

from app.services.schema_validator import SchemaValidator

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
    
    dataset = DatasetRepository.create(
        db=db,
        filename=file.filename
    )

    columns = CSVService.get_columns(file.file)
    validation_result = SchemaValidator.validate(columns)

    return {
    "dataset_id": str(dataset.id),
    "filename": file.filename,
    "columns": columns,
    "validation": validation_result
}