"""
Light wrapper for the Supabase client. This file creates a client when
`SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` (or `SUPABASE_KEY`) are set.

Notes:
- Use `SUPABASE_SERVICE_ROLE_KEY` or server-only key for admin operations.
- Do NOT expose service role key in the browser.
"""
import os
from typing import Optional

try:
    from supabase import create_client
except Exception:
    create_client = None

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_KEY") or os.getenv("SUPABASE_ANON_KEY")

supabase = None
if create_client and SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_supabase_client() -> Optional[object]:
    return supabase
