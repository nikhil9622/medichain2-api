from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select
from app.database import get_session
from app.models import Unit, Batch
from app.utils.ai_utils import compute_anomaly_score
from app.database import get_session

router = APIRouter()

@router.get("/", summary="Verify a UDI")
def verify(udi: str = Query(...)):
    session = next(get_session())
    stmt = select(Unit).where(Unit.udi == udi)
    u = session.exec(stmt).first()
    if not u:
        return {"exists": False, "udi": udi, "verdict": "NOT_FOUND"}
    stmt2 = select(Batch).where(Batch.id == u.batch_id)
    b = session.exec(stmt2).first()
    # create simple features from udi and batch for demo
    features = [len(udi), sum(ord(c) for c in udi) % 100, 0.0]
    score, pred = compute_anomaly_score(features)
    verdict = "AUTHENTIC" if pred == 1 else "SUSPICIOUS"
    return {
        "exists": True,
        "udi": u.udi,
        "product_name": b.product_name if b else None,
        "batch_code": b.batch_code if b else None,
        "mfg_date": b.mfg_date if b else None,
        "exp_date": b.exp_date if b else None,
        "metadata_hash": u.metadata_hash,
        "qr_path": u.qr_path,
        "anomaly_score": score,
        "verdict": verdict
    }
