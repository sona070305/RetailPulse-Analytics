from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Change 'from app.api.endpoints' to 'from backend.app.api.endpoints'
from backend.app.api.endpoints import router as api_router

app = FastAPI(
    title="RetailPulse API Engine",
    description="Backend Service Engine for Retail Analytics & Demand Prediction",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "Online", "service": "RetailPulse FastAPI Core Engine"}