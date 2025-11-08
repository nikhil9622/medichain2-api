from sqlmodel import SQLModel, create_engine, Session
import os

# Require Supabase/Postgres URL from environment for production deployments.
# Use SUPABASE_DB_URL or DATABASE_URL. Do NOT fall back to SQLite in this
# configuration to avoid accidental local persistence when deploying to Vercel.
DATABASE_URL = os.getenv("SUPABASE_DB_URL") or os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "No SUPABASE_DB_URL or DATABASE_URL environment variable found. "
        "Set SUPABASE_DB_URL to your Supabase/Postgres connection URL (postgresql://user:pass@host:5432/dbname)."
    )

# Create engine for Postgres (SQLModel/SQLAlchemy will handle it).
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
