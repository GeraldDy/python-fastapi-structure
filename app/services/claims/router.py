from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps.db import get_db

from app.services.claims.schemas import ClaimCreate, ClaimOut
from app.services.claims.service import ClaimsService

router = APIRouter()

@router.post("/", response_model=ClaimOut)
def create_claim(data: ClaimCreate, db: Session = Depends(get_db)):
    return ClaimsService.create_claim(db, data)

@router.get("/", response_model=list[ClaimOut])
def list_claims(db: Session = Depends(get_db)):
    return ClaimsService.list_claims(db)
