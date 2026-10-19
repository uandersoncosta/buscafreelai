from app.database.db import SessionLocal
from app.models.profile import Profile
from app.services.project_service import save_project
from app.services.search_service import generate_search_queries
from app.scrapers.workana import search_workana_projects


def search_and_save_profile_projects(profile_id: int,) -> int:
    db = SessionLocal()

    try:
        profile = db.get(Profile, profile_id)

        if not profile:
            raise ValueError(
                f"Perfil {profile_id} não encontrado."
            )

        queries = generate_search_queries(profile)

        total_processed = 0

        for query in queries:
            import asyncio

            projects = asyncio.run(
                search_workana_projects(query)
            )

            for project_data in projects:
                save_project(
                    db=db,
                    project_data=project_data,
                )

                total_processed += 1

        return total_processed

    finally:
        db.close()