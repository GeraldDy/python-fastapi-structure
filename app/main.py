from fastapi import FastAPI
from app.api.routers import api_router
from app.core.database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI SOA Boilerplate")

app.include_router(api_router)
