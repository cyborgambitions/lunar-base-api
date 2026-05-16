from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/lockheed-martin")
async def get_lockheed_martin():
    return {
        "company": "Lockheed Martin",
        "ticker": "LMT",
        "price": 478.25,
        "change_percent": 1.34,
        "market_cap": 112.4,
        "sector": "Aerospace & Defense",
        "lunar_relevance": "Major contractor for Artemis program and lunar habitats",
        "last_updated": datetime.now().isoformat()
    }


@router.get("/spacex")
async def get_spacex():
    """SpaceX is private — we return curated impact data"""
    return {
        "company": "SpaceX",
        "status": "Private",
        "estimated_valuation": 210,  # billions
        "key_projects": ["Starship", "Starlink", "NASA Artemis"],
        "lunar_impact": "Starship is critical for Moon Alpha Base logistics and heavy cargo",
        "recent_news": "Starship Flight 9 successful - lunar landing timeline accelerating",
        "last_updated": datetime.now().isoformat()
    }


@router.get("/rocket-lab")
async def get_rocket_lab():
    return {
        "company": "Rocket Lab",
        "ticker": "RKLB",
        "price": 28.45,
        "change_percent": 3.12,
        "market_cap": 14.2,
        "lunar_relevance": "Neutron rocket positioned for lunar payload delivery",
        "last_updated": datetime.now().isoformat()
    }
