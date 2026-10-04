# Busca-Freelaí

Sistema de recomendação de projetos da Workana baseado no perfil profissional do usuário.

## Objetivo

O Buscafreelai busca projetos disponíveis na Workana e utiliza inteligência artificial para analisar a compatibilidade entre os requisitos dos projetos e o perfil profissional do usuário.

## Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Playwright
- BeautifulSoup
- Agno
- Google Gemini
- Docker

## Status

🚧 Em desenvolvimento.

## Estrutura

```text
buscafrelai/
├── app/
│   ├── api/
│   │   └── routes/
│   ├── agents/
│   ├── scrapers/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── tests/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
