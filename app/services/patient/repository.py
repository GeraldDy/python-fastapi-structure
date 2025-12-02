from sqlalchemy.orm import Session
from app.models.patient import Patient

class PatientRepository:

    @staticmethod
    def create(db: Session, data):
        obj = Patient(**data.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_all(db: Session):
        return db.query(Patient).all()
