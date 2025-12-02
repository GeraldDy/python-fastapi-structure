from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps.db import get_db

from app.services.admission.schemas import AdmissionCreate, AdmissionOut
from app.services.admission.service import AdmissionService

router = APIRouter()

@router.post("/", response_model=AdmissionOut)
def create_admission(data: AdmissionCreate, db: Session = Depends(get_db)):
    return AdmissionService.create_admission(db, data)

@router.get("/", response_model=list[AdmissionOut])
def list_admission(db: Session = Depends(get_db)):
    return AdmissionService.list_admissions(db)
