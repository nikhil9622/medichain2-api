from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Manufacturer(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    name: str
    email: Optional[str] = None
    api_key: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Batch(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    manufacturer_id: str
    batch_code: str
    product_name: str
    mfg_date: Optional[str] = None
    exp_date: Optional[str] = None
    metadata_json: Optional[str] = None
    metadata_hash: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Unit(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    udi: str = Field(sa_column_kwargs={"unique": True})
    batch_id: str
    status: str = "MINTED"
    metadata_hash: Optional[str] = None
    qr_path: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class VerificationLog(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    udi: str
    user_identifier: Optional[str] = None
    result: str
    ai_score: Optional[float] = None
    tx_hash: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
