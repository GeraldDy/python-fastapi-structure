from sqlalchemy.orm import Session
from app.services.admission.repository import AdmissionRepository

class AdmissionService:

    @staticmethod
    def create_admission(db: Session, data):
        return AdmissionRepository.create(db, data)

    @staticmethod
    def list_admissions(db: Session):
        return AdmissionRepository.get_all(db)
