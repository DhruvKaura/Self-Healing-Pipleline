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

    df = CSVService.read_csv(file.file)

    columns = CSVService.get_columns(df)
    validation_result = SchemaValidator.validate(columns)

    mapping = None

    if not validation_result["valid"]:
        mapping = HealingService.generate_mapping(
            expected_columns=SchemaValidator.EXPECTED_SCHEMA,
            actual_columns=columns
        )

    healed_validation = None

    if mapping:
        healed_df = CSVService.apply_mapping(
            df=df,
            mapping=mapping
        )
    healed_columns = CSVService.get_columns(
        healed_df
    )

    healed_validation = SchemaValidator.validate(
        healed_columns
    )
    return {
        "dataset_id": str(dataset.id),
        "filename": file.filename,
        "original_columns": columns,
        "validation": validation_result,
        "mapping": mapping,
        "healed_validation": healed_validation
    }