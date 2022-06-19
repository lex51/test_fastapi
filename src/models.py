from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from pydantic import BaseModel


class Email(BaseModel):

    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    uuid = Column(UUID)
    email = Column(String)
