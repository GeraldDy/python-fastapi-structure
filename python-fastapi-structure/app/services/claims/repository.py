from sqlalchemy.orm import Session
from app.models.claims import Claim

class ClaimsRepository:

    @staticmethod
    def create(db: Session, data):
        obj = Claim(**data.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_all(db: Session):
        return db.query(Claim).all()
