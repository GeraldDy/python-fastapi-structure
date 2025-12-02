from sqlalchemy.orm import Session
from app.services.claims.repository import ClaimsRepository

class ClaimsService:

    @staticmethod
    def create_claim(db: Session, data):
        return ClaimsRepository.create(db, data)

    @staticmethod
    def list_claims(db: Session):
        return ClaimsRepository.get_all(db)
