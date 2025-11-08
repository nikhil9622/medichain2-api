from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
import json, hashlib, uuid
from app.database import get_session
from app.models import Batch, Unit
from app.utils.auth_utils import require_api_key
from app.utils.qr_utils import make_qr
from sqlmodel import Session

router = APIRouter()

class MintRequest(BaseModel):
    product_name: str
    batch_code: str
    mfg_date: Optional[str] = None
    exp_date: Optional[str] = None
    qty: int = 1
    metadata: dict | None = None

def compute_hash(obj) -> str:
    j = json.dumps(obj, sort_keys=True).encode()
    return hashlib.sha256(j).hexdigest()

def generate_udi():
    return "mc-" + hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()[:24]

@router.post("/", summary="Mint a batch and generate unit UDIs")
def mint(req: MintRequest, manufacturer=Depends(require_api_key)):
    metadata = req.metadata or {}
    metadata.update({"product_name": req.product_name, "batch_code": req.batch_code})
    mh = compute_hash(metadata)
    session = next(get_session())
    batch = Batch(manufacturer_id=manufacturer.id, batch_code=req.batch_code,
                  product_name=req.product_name, mfg_date=req.mfg_date,
                  exp_date=req.exp_date, metadata_json=json.dumps(metadata), metadata_hash=mh)
    session.add(batch); session.commit(); session.refresh(batch)
    created = []
    for i in range(req.qty):
        udi = generate_udi()
        unit = Unit(udi=udi, batch_id=batch.id, metadata_hash=mh)
        session.add(unit); session.commit(); session.refresh(unit)
        qrpath = make_qr(udi)
        unit.qr_path = qrpath
        session.add(unit); session.commit()
        created.append({"udi": udi, "qr_path": qrpath})
    return {"batch_id": batch.id, "metadata_hash": mh, "created": created}
