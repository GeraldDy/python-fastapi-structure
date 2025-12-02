from pydantic import BaseModel

class PatientCreate(BaseModel):
    firstname: str
    lastname: str

class PatientOut(BaseModel):
    id: int
    firstname: str
    lastname: str

    class Config:
        orm_mode = True
