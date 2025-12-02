from fastapi import APIRouter

from app.services.admission.router import router as admission_router
from app.services.patient.router import router as patient_router
from app.services.claims.router import router as claims_router

api_router = APIRouter()

api_router.include_router(admission_router, prefix="/admission", tags=["Admission"])
api_router.include_router(patient_router, prefix="/patient", tags=["Patient"])
api_router.include_router(claims_router, prefix="/claims", tags=["Claims"])
