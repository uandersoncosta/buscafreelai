from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.project import Project


def save_project(db: Session,project_data: Project,):
    existing_project = db.scalar(
        select(Project).where(
            Project.url == str(project_data.url)
        )
    )

    if existing_project:
        existing_project.title = project_data.title
        existing_project.conteudo = project_data.conteudo
        existing_project.qnt_propostas = (
            project_data.qnt_propostas
        )
        existing_project.valor = project_data.valor
        existing_project.skills = project_data.skills

        db.commit()
        db.refresh(existing_project)

        return existing_project

    project = Project(
        title=project_data.title,
        url=str(project_data.url),
        conteudo=project_data.conteudo,
        qnt_propostas=project_data.qnt_propostas,
        valor=project_data.valor,
        skills=project_data.skills,
        analise=project_data.analise,
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project