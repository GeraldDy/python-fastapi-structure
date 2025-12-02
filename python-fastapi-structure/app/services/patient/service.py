from sqlalchemy.orm import Session
from app.services.patient.repository import PatientRepository

class PatientService:

    @staticmethod
    def create_patient(db: Session, data):
        return PatientRepository.create(db, data)

    @staticmethod
    def list_patients(db: Session):
        return PatientRepository.get_all(db)
