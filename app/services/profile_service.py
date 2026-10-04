from sqlalchemy.orm import Session

from app.schemas.profile import Profile


def create_profile(
    db: Session,
    profile_data: Profile,
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