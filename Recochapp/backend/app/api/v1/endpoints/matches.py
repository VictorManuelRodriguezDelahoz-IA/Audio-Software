from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Match])
def read_matches(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Ver todos los partidos disponibles (recochas).
    """
    matches = db.query(models.Match).offset(skip).limit(limit).all()
    return matches

@router.post("/", response_model=schemas.Match)
def create_match(
    *,
    db: Session = Depends(deps.get_db),
    match_in: schemas.MatchCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Crear una nueva recocha.
    """
    match = models.Match(**match_in.model_dump(), organizer_id=current_user.id)
    db.add(match)
    db.commit()
    db.refresh(match)
    return match