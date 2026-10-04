import os
import time

from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv

from app.schemas.profile import Profile
from app.schemas.project import Project

load_dotenv()

agent = Agent(
    model=Gemini(
        id="gemini-3.5-flash",
        api_key=os.getenv("GOOGLE_API_KEY"),
    ),
    instructions=[
        "Você é um especialista em análise de compatibilidade profissional.",
        "Compare o perfil do profissional com o projeto freelancer.",
        "Considere principalmente as skills, experiência e categoria desejada.",
        "Dê uma nota de compatibilidade de 0 a 100.",
        "Explique objetivamente os motivos da nota.",
        "Não invente experiência ou tecnologias que não estejam no perfil.",
    ],
)

def analyze_project(profile: Profile, project: Project, max_retries: int = 3,) -> tuple[int, str]:
    prompt = f"""
Analise a compatibilidade entre o profissional e o projeto.

PROFISSIONAL

Nome:
{profile.nome}

Skills:
{", ".join(profile.skills)}

Experiência:
{profile.experiencia}

Categorias desejadas:
{", ".join(profile.desired_categories)}


PROJETO

Título:
{project.title}

Descrição:
{project.conteudo}

Skills exigidas:
{", ".join(project.skills)}

Valor:
{project.valor}

Retorne exatamente neste formato:

SCORE: número entre 0 e 100
ANALISE: explicação objetiva da compatibilidade
"""

    last_error = None

    for attempt in range(max_retries):
        try:
            response = agent.run(prompt)

            content = response.content

            if not content:
                raise ValueError("O modelo retornou uma resposta vazia.")

            content = content.strip()

            score_line = next(
                line
                for line in content.splitlines()
                if line.upper().startswith("SCORE:")
            )

            analysis_line = next(
                line
                for line in content.splitlines()
                if line.upper().startswith("ANALISE:")
            )

            score = int(
                score_line.split(":", 1)[1].strip()
            )

            analysis = (
                analysis_line
                .split(":", 1)[1]
                .strip()
            )

            if not 0 <= score <= 100:
                raise ValueError(
                    f"Score fora do intervalo permitido: {score}"
                )

            return score, analysis

        except Exception as error:
            last_error = error

            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)

    raise RuntimeError(
        f"Não foi possível analisar o projeto "
        f"após {max_retries} tentativas."
    ) from last_error