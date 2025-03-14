from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import engine
from app.models.models import Project
from app.models.schemas import ProjectCreate, ProjectUpdate
from app.security.dependencies import require_role

router = APIRouter()

@router.post("/", dependencies=[Depends(require_role("admin"))])
def create_project(project: ProjectCreate):
    with Session(engine) as session:
        new_project = Project(name=project.name, description=project.description)
        session.add(new_project)
        session.commit()
    return {"message": "Project created successfully"}

@router.get("/")
def get_projects():
    with Session(engine) as session:
        projects = session.exec(select(Project)).all()
    return projects
