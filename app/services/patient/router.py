from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps.db import get_db

from app.services.patient.schemas import PatientCreate, PatientOut
from app.services.patient.service import PatientService

router = APIRouter()

@router.post("/", response_model=PatientOut)
def create_patient(data: PatientCreate, db: Session = Depends(get_db)):
    return PatientService.create_patient(db, data)

@router.get("/", response_model=list[PatientOut])
def list_patients(db: Session = Depends(get_db)):
    return PatientService.list_patients(db)
