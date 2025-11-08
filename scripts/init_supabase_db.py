"""Run this script locally (with SUPABASE_DB_URL set) to create tables on the
Supabase/Postgres database using SQLModel's metadata.

Usage (PowerShell):
$env:SUPABASE_DB_URL = "postgresql://<user>:<pass>@<host>:5432/<db>?sslmode=require"
python scripts/init_supabase_db.py
"""
import os
import sys

from app.database import init_db


def main():
    db_url = os.getenv("SUPABASE_DB_URL") or os.getenv("DATABASE_URL")
    if not db_url:
        print("ERROR: SUPABASE_DB_URL or DATABASE_URL not set in environment.")
        sys.exit(1)
    print("Using DB URL:", db_url)
    init_db()
    print("init_db() finished — tables created (or already existed).")


if __name__ == "__main__":
    main()
