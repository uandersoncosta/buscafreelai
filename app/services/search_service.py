from app.agents.matcher import agent
from app.models.profile import Profile


def generate_search_queries(profile: Profile) -> list[str]:

    prompt = f"""
Analise o perfil profissional abaixo e gere até 3
consultas para pesquisar projetos na Workana.

Nome: {profile.nome}
Skills: {", ".join(profile.skills)}
Experiência: {profile.experiencia}
Categorias desejadas: {", ".join(profile.desired_categories)}

Regras:
- Priorize tecnologias presentes no perfil.
- Considere a experiência e as categorias desejadas.
- Cada consulta deve ser curta e específica.
- Não repita consultas equivalentes.
- Retorne somente uma consulta por linha.
- Não inclua numeração, explicações ou Markdown.
"""

    response = agent.run(prompt)
    
    content = response.content or ""

    queries = [
        line.strip()
        for line in content.splitlines()
        if line.strip()
    ]

    return queries[:3]