from pydantic import BaseModel

class ClaimCreate(BaseModel):
    claim_code: str
    description: str

class ClaimOut(BaseModel):
    id: int
    claim_code: str
    description: str

    class Config:
        orm_mode = True
