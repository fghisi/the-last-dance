import datetime

from uuid import uuid5

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime


class BaseModel(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid5)
    created_at = Column(
        DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = Column(DateTime(timezone=True), nullable=True)


Base = declarative_base(cls=BaseModel)
