import os
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
from app.scrapers.workana import search_workana_projects

load_dotenv()

def search_workana(query: str) -> list[dict]:
  """
  Pesquisa projetos na Workana usando uma query.
  """
  import asyncio

  projects = asyncio.run(search_workana_projects(query))

  return [
    project.model_dump(mode="json")
    for project in projects
  ]


agent = Agent(
    model=Gemini(
      id="gemini-3.5-flash",
      api_key=os.getenv("GOOGLE_API_KEY"),
    ),
    tools=[search_workana],
    instructions=[
      "Você é um especialista em encontrar projetos freelancer.",
      "Analise o perfil profissional fornecido.",
      "Utilize a ferramenta search_workana para pesquisar projetos.",
      "Escolha queries relevantes para o perfil.",
      "Não faça pesquisas genéricas.",
      "Priorize tecnologias e competências do perfil.",
    ],
)