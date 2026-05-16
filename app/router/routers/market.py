from fastapi import APIRouter

router = APIRouter()

@router.get("/overview")
async def get_market_overview():
    return {
        "timestamp": "2026-05-16T08:05:00Z",
        "market_status": "Open",
        "total_market_cap": 124.7,  # in billions
        "top_gainers": [
            {"ticker": "RKLB", "change": 4.2},
            {"ticker": "ASTS", "change": 3.8}
        ],
        "lunar_index": 142.3
    }
