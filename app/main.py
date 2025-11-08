from fastapi import FastAPI
from app.routes import onboard, mint, verify, log, admin

app = FastAPI(title="MediChain2")

# include routers
app.include_router(onboard.router, prefix="/onboard", tags=["onboard"])
app.include_router(mint.router, prefix="/mint", tags=["mint"])
app.include_router(verify.router, prefix="/verify", tags=["verify"])
app.include_router(log.router, prefix="/log", tags=["log"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])


@app.get("/")
def root():
    return {"message": "MediChain2 API (with mint/verify) is online"}
