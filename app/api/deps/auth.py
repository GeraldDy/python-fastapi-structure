from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer

security = HTTPBearer()

def dummy_auth(token: str = Depends(security)):
    if token.credentials != "secret-token":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return True