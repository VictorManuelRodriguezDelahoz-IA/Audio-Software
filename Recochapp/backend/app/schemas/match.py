from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class MatchBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime
    location_name: str
    price_per_person: float = 0.0
    players_total: int = 10

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int
    organizer_id: int
    players_current: int

    class Config:
        from_attributes = True