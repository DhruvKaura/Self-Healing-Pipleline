from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid


from app.core.database import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    filename = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False,
        default="uploaded"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )