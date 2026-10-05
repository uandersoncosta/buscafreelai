from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.UserProfile import UserProfile


def create_profile(
    db: Session,
    profile_data: UserProfile,
) -> Profile:

    profile = Profile(
        nome=profile_data.nome,
        skills=profile_data.skills,
        experiencia=profile_data.experiencia,
        desired_categories=profile_data.desired_categories,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile