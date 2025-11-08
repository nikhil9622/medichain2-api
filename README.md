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
