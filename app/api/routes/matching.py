from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.schemas.match import (MatchingRequest, MatchingResponse)
from app.services.matching_service import (validate_matching_profile, process_saved_projects)
from app.services.workana_service import (search_and_save_profile_projects)

router = APIRouter(prefix="/matching", tags=["Matching"])

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MatchingResponse)
def start_matching(request: MatchingRequest, db: Session = Depends(get_db)):
    try:
        validate_matching_profile(
            db=db,
            profile_id=request.profile_id,
        )

        db.close()

        total_projects = search_and_save_profile_projects(
            profile_id=request.profile_id,
        )

        db = SessionLocal()

        matches = process_saved_projects(
            db=db,
            profile_id=request.profile_id,
        )

        return MatchingResponse(
            profile_id=request.profile_id,
            message=(
                f"Busca concluída. "
                f"{total_projects} projetos processados "
                f"na busca e {len(matches)} matches analisados."
            ),
        )

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )