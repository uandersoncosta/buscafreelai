from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.match import Match
from app.models.profile import Profile
from app.models.project import Project
from app.services.ai_service import analyze_project


def save_match(db: Session, profile_id: int, project_id: int, score: int, analise: str,) -> Match:

    existing_match = db.scalar(
        select(Match).where(
            Match.profile_id == profile_id,
            Match.project_id == project_id,
        )
    )

    if existing_match:
        existing_match.score = score
        existing_match.analise = analise

        db.commit()
        db.refresh(existing_match)

        return existing_match

    match = Match(
        profile_id=profile_id,
        project_id=project_id,
        score=score,
        analise=analise,
    )

    db.add(match)
    db.commit()
    db.refresh(match)

    return match


def analyze_and_save_match(db: Session, profile_id: int, project_id: int,) -> Match:
    profile = db.get(Profile, profile_id)

    if not profile:
        raise ValueError(
            f"Perfil {profile_id} não encontrado."
        )

    project = db.get(Project, project_id)

    if not project:
        raise ValueError(
            f"Projeto {project_id} não encontrado."
        )

    score, analise = analyze_project(
        profile=profile,
        project=project,
    )

    return save_match(
        db=db,
        profile_id=profile_id,
        project_id=project_id,
        score=score,
        analise=analise,
    )