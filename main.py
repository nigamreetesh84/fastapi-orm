from sqlalchemy.orm import sessionmaker, declarative_base, relationship,Session
from enum import Enum as PyEnum
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from datetime import datetime
from models import *
import crud

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clients")
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.create_client(db=db, client=client)
    return db_client

@app.get("/clients")
def get_all_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients

@app.get("/clients/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@app.post("/workflows")
def create_workflow(workflow: WorkflowCreate, db: Session = Depends(get_db)):
    db_workflow = crud.create_workflow(db=db, workflow=workflow)
    return db_workflow

@app.get("/workflows")
def get_all_workflows(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workflows = crud.get_workflows(db, skip=skip, limit=limit)
    return workflows

@app.get("/workflows/{workflow_id}")
def get_workflow(workflow_id: int, db: Session = Depends(get_db)):
    db_workflow = crud.get_workflow(db, workflow_id=workflow_id)
    if db_workflow is None:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return db_workflow

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
