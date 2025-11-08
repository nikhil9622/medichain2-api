from fastapi import APIRouter
from pydantic import BaseModel
from app.database import get_session
from app.models import VerificationLog

router = APIRouter()

class LogRequest(BaseModel):
    udi: str
    user_identifier: str | None = None
    result: str
    ai_score: float | None = None
    tx_hash: str | None = None

@router.post("/", summary="Store verification log")
def log_event(req: LogRequest):
    session = next(get_session())
    entry = VerificationLog(udi=req.udi, user_identifier=req.user_identifier,
                            result=req.result, ai_score=req.ai_score, tx_hash=req.tx_hash)
    session.add(entry); session.commit(); session.refresh(entry)
    return {"id": entry.id, "status": "logged"}
