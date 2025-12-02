from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    claim_code = Column(String)
    description = Column(String)
