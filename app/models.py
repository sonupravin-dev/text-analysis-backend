from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Batch(Base):
    __tablename__ = "batches"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(String)
    status = Column(String)

class BatchItem(Base):
    __tablename__ = "batch_items"

    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(Integer)
    text = Column(Text)
    status = Column(String)
    result = Column(Text, nullable=True)
    error = Column(Text, nullable=True)