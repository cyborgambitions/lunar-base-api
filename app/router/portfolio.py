from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Position(BaseModel):
    ticker: str
    shares: int
    avg_price: float

class PortfolioSimulation(BaseModel):
    positions: List[Position]

@router.post("/simulate")
async def simulate_portfolio(data: PortfolioSimulation):
    # Simple simulation logic (you can expand this)
    total_value = 0
    for pos in data.positions:
        current_price = 28.45 if pos.ticker == "RKLB" else 478.25  # placeholder
        total_value += pos.shares * current_price

    return {
        "total_value": round(total_value, 2),
        "return_percent": 12.4,
        "message": "Simulation complete. Connect live prices for accuracy."
    }
