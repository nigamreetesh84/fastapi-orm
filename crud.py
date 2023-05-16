from sqlalchemy.orm import Session
import models


def create_workflow(db: Session, workflow: models.WorkflowCreate):
    db_workflow = models.Workflow(**workflow.dict())
    db.add(db_workflow)
    db.commit()
    db.refresh(db_workflow)
    return db_workflow


def get_workflows(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Workflow).offset(skip).limit(limit).all()


def get_workflow(db: Session, workflow_id: int):
    return db.query(models.Workflow).filter(models.Workflow.id == workflow_id).first()


# def update_workflow(db: Session, workflow_id: int, workflow: WorkflowUpdate):
#     db_workflow = db.query(models.Workflow).filter(models.Workflow.id == workflow_id).first()
#     if db_workflow:
#         for field, value in workflow.dict(exclude_unset=True).items():
#             setattr(db_workflow, field, value)
#         db.commit()
#         db.refresh(db_workflow)
#         return db_workflow


# def delete_workflow(db: Session, workflow_id: int):
#     db.query(models.Workflow).filter(models.Workflow.id == workflow_id).delete()
#     db.commit()



def create_client(db: Session, client: models.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


# def update_client(db: Session, client_id: int, client: ClientUpdate):
#     db_client = db.query(models.Client).filter(models.Client.id == client_id).first()
#     if db_client:
#         for field, value in client.dict(exclude_unset=True).items():
#             setattr(db_client, field, value)
#         db.commit()
#         db.refresh(db_client)
#         return db_client


# def delete_client(db: Session, client_id: int):
#     db.query(models.Client).filter(models.Client.id == client_id).delete()
#     db.commit()