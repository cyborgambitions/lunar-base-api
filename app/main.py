from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import market, companies, portfolio

app = FastAPI(
    title="Moon Alpha Base - Space Economy Dashboard",
    description="Real-time lunar & space economy market data",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(market.router, prefix="/api/market", tags=["Market"])
app.include_router(companies.router, prefix="/api/companies", tags=["Companies"])
app.include_router(portfolio.router, prefix="/api/portfolio", tags=["Portfolio"])

@app.get("/")
async def root():
    return {"message": "Moon Alpha Base Dashboard API is running"}
