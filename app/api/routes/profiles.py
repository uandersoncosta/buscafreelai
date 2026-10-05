from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.schemas.UserProfile import UserProfile
from app.services.profile_service import create_profile


router = APIRouter(
    prefix="/profiles",
    tags=["Profiles"],
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_profile_endpoint(
    profile_data: UserProfile,
    db: Session = Depends(get_db),
):
    profile = create_profile(
        db=db,
        profile_data=profile_data,
    )

    return {
        "id": profile.id,
        "nome": profile.nome,
        "skills": profile.skills,
        "experiencia": profile.experiencia,
        "desired_categories": profile.desired_categories,
    }