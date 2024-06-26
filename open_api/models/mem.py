import uuid

from sqlalchemy import Column, String

from .base import Base


class Mem(Base):
    __tablename__ = 'mems'

    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = Column(String(1000), default='')
    url = Column(String(250), nullable=True)
    file_extension = Column(String(20))
