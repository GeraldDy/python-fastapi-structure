from pydantic import BaseModel

class AdmissionCreate(BaseModel):
    hospital_code: str
    patient_name: str

class AdmissionOut(BaseModel):
    id: int
    hospital_code: str
    patient_name: str

    class Config:
        orm_mode = True
