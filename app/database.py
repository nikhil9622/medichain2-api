from sqlmodel import SQLModel, create_engine, Session
import os

# Require Supabase/Postgres URL from environment for production deployments.
# Use SUPABASE_DB_URL or DATABASE_URL. Do NOT fall back to SQLite in this
# configuration to avoid accidental local persistence when deploying to Vercel.
DATABASE_URL = os.getenv("SUPABASE_DB_URL") or os.getenv("DATABASE_URL")
if not DATABASE_URL:
    # Do not raise at import time — allow the app to start even if DB isn't configured.
    # This prevents serverless processes from exiting during deployment when env
    # variables are not yet set. Functions that require DB will raise at call time.
    engine = None
else:
    # Create engine for Postgres (SQLModel/SQLAlchemy will handle it).
    engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)


def init_db():
    if engine is None:
        raise RuntimeError("Database engine not configured. Set SUPABASE_DB_URL or DATABASE_URL.")
    SQLModel.metadata.create_all(engine)


def get_session():
    if engine is None:
        raise RuntimeError("Database engine not configured. Set SUPABASE_DB_URL or DATABASE_URL.")
    with Session(engine) as session:
        yield session
