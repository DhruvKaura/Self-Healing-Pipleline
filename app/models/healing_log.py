import uuid
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Text

from app.core.database import Base


class HealingLog(Base):
    __tablename__ = "healing_logs"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    dataset_id = Column(
        String,
        nullable=False
    )

    original_columns = Column(
        Text,
        nullable=False
    )

    generated_mapping = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )