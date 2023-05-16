from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy import create_engine, Column, Integer, String, Enum, Text, DateTime, ForeignKey

from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.sql import func
from typing import Optional
from enum import Enum as PyEnum
from datetime import datetime
from pydantic import BaseModel

engine = create_engine("sqlite:///mydatabase.db")  # Replace with your database file path
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ClientStatus(str, PyEnum):
    active = "active"
    inactive = "inactive"

class WorkflowStatus(str, PyEnum):
    success = "success"
    fail = "fail"

class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String, unique=True, index=True)
    name = Column(String)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(Enum(ClientStatus))

    workflows = relationship("Workflow", back_populates="client")

class Workflow(Base):
    __tablename__ = "workflow"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("client.id"))
    status = Column(Enum(WorkflowStatus))
    message = Column(Text)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    client = relationship("Client", back_populates="workflows")

Base.metadata.create_all(bind=engine)

class ClientCreate(BaseModel):
    client_id: int
    name: str
    status: ClientStatus

class WorkflowCreate(BaseModel):
    client_id: int
    status: WorkflowStatus
    message: str

class ClientDetails(BaseModel):
    id: int
    client_id: str
    name: str
    created_date: datetime
    updated_date: datetime
    status: ClientStatus

class WorkflowDetails(BaseModel):
    id: int
    client_id: int
    status: WorkflowStatus
    message: str
    created_date: datetime
    updated_date: datetime
