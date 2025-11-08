import secrets
from fastapi import Header, HTTPException, Depends
from sqlmodel import select
from app.database import get_session
from app.models import Manufacturer

def generate_api_key():
    return "mk-" + secrets.token_hex(16)

def require_api_key(x_api_key: str = Header(...)):
    # used for manufacturer endpoints
    session = next(get_session())
    stmt = select(Manufacturer).where(Manufacturer.api_key == x_api_key)
    m = session.exec(stmt).first()
    if not m:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return m
