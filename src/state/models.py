from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Change(Base):
    __tablename__ = "changes"
    id = Column(Integer, primary_key=True)
    commit = Column(String)
    service = Column(String)
    timestamp = Column(String)
    summary = Column(String)

class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True)
    service = Column(String)
    timestamp = Column(String)
    value = Column(Float)
