# MediChain2 API (FastAPI) — Vercel-ready

This repository contains a small FastAPI app intended for deployment on Vercel. The FastAPI app entrypoint is `app/main.py` (configured in `vercel.json`).

Quick files:

- `app/main.py` — FastAPI application with endpoints `/`, `/onboard`, `/mint`, `/verify`, `/log`.
- `requirements.txt` — Python dependencies.
- `vercel.json` — Vercel build & routing configuration.
- `.gitignore` — Useful ignores.

Run locally (optional):

1. Create and activate a virtualenv.
2. Install deps:

```powershell
python -m pip install -r requirements.txt
```

3. Run with uvicorn locally:

```powershell
python -m uvicorn app.main:app --reload --port 8000
```

Visit `http://localhost:8000/` and test endpoints, e.g. `/onboard`, `/mint` (requires API key), `/verify`, `/log`.

Deploy to Vercel:

1. Push this repo to GitHub (already done).
2. On https://vercel.com, import the repo and deploy — Vercel will detect Python and use `app/main.py` per `vercel.json`.

---

## Supabase configuration (Postgres)

This project uses Supabase (Postgres) as the primary database. Do NOT commit your keys into the repo. Instead, set the following environment variables in Vercel (Project → Settings → Environment Variables) and locally for testing:

- `SUPABASE_URL` — e.g. `https://<project>.supabase.co` (public project URL)
- `SUPABASE_ANON_KEY` — public anon key for client-side (only safe if RLS is enforced)
- `SUPABASE_SERVICE_ROLE_KEY` — server-side service role key (POWERFUL — keep secret)
- `SUPABASE_DB_URL` — Postgres connection string for SQLModel (required for server):
  - Example: `postgresql://<user>:<pass>@db.<region>.supabase.co:5432/postgres?sslmode=require`

### Local init (create tables)

1. Copy `.env.template` to `.env` and fill values, or set env vars in your shell.
2. Run the initializer script (PowerShell example):

```powershell
$env:SUPABASE_DB_URL = "postgresql://<user>:<pass>@<host>:5432/<db>?sslmode=require"
python scripts/init_supabase_db.py
```

This will call `init_db()` and create the SQLModel tables in your Supabase Postgres database.

### Front-end usage

- See `web/supabaseClient.js` for a small example of creating a Supabase client using `SUPABASE_URL` and `SUPABASE_ANON_KEY`.

### Security notes

- NEVER store `SUPABASE_SERVICE_ROLE_KEY` or `SUPABASE_DB_URL` directly in your public repository. Use Vercel's environment variables for production.
- If you want me to initialize the database remotely, you can run the `scripts/init_supabase_db.py` yourself with the env var set, or paste the `SUPABASE_DB_URL` here (not recommended since it's a secret).
# MediChain API (FastAPI) — Vercel-ready

This repository contains a tiny FastAPI app intended for deployment on Vercel. The FastAPI app lives at `api/index.py` (Vercel's Serverless Function entrypoint).

Quick files:

- `api/index.py` — FastAPI application with endpoints `/` and `/verify`.
- `requirements.txt` — Python dependencies (fastapi, uvicorn).
- `vercel.json` — Vercel build & routing configuration.
- `.gitignore` — Useful ignores.

Run locally (optional):

1. Create and activate a virtualenv.
2. Install deps:

```powershell
python -m pip install -r requirements.txt
```

3. Run with uvicorn:

```powershell
python -m uvicorn api.index:app --reload --port 8000
```

Visit `http://localhost:8000/` and `http://localhost:8000/verify?udi=mc-12345`

Deploy to Vercel:

1. Push this repo to GitHub.
2. On https://vercel.com, import the repo and deploy — Vercel will detect Python and use `api/index.py` per `vercel.json`.
