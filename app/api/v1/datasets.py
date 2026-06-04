from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.dataset_repository import DatasetRepository

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