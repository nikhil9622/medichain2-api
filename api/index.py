from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MediChain API is online on Vercel!"}


@app.get("/verify")
def verify(udi: str = Query(...)):
    if udi.startswith("mc-"):
        return {
            "exists": True,
            "udi": udi,
            "product_name": "DemoAmox 500",
            "batch_code": "A1001",
            "mfg_date": "2025-11-01",
            "exp_date": "2027-11-01",
            "anomaly_score": 0.12,
            "verdict": "AUTHENTIC"
        }
    return JSONResponse({"exists": False, "verdict": "COUNTERFEIT"}, status_code=404)
