from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Admission(Base):
    __tablename__ = "admissions"

    id = Column(Integer, primary_key=True, index=True)
    hospital_code = Column(String)
    patient_name = Column(String)
