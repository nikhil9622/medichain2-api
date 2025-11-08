from fastapi import APIRouter, Header, HTTPException
import os
from app.database import init_db

router = APIRouter()

@router.post("/init-db", summary="Run database init (protected)")
def init_db_endpoint(x_init_token: str | None = Header(None)):
    """Protected endpoint to initialize the database tables remotely.

    To use:
    - Set an environment variable `INIT_SECRET` in Vercel to a strong secret.
    - Call POST /admin/init-db with header `x-init-token: <INIT_SECRET>`.
    """
    secret = os.getenv("INIT_SECRET")
    if not secret:
        raise HTTPException(status_code=403, detail="Admin init not configured")
    if not x_init_token or x_init_token != secret:
        raise HTTPException(status_code=401, detail="Invalid init token")

    init_db()
    return {"status": "ok", "message": "init_db() executed"}
