from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database import init_db, get_session
from app.models import Manufacturer
from app.utils.auth_utils import generate_api_key
from sqlmodel import Session

router = APIRouter()
init_db()  # ensure DB exists

class OnboardRequest(BaseModel):
    name: str
    email: str | None = None

@router.post("/", summary="Onboard a manufacturer (returns API key)")
def onboard(req: OnboardRequest):
    api_key = generate_api_key()
    m = Manufacturer(name=req.name, email=req.email, api_key=api_key)
    session = next(get_session())
    session.add(m); session.commit(); session.refresh(m)
    return {"manufacturer_id": m.id, "api_key": api_key}
