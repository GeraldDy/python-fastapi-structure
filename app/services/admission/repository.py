from sqlalchemy.orm import Session
from app.models.admission import Admission

class AdmissionRepository:

    @staticmethod
    def create(db: Session, data):
        obj = Admission(**data.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_all(db: Session):
        return db.query(Admission).all()
