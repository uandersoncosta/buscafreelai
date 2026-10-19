from fastapi import FastAPI
from app.api.routes.profiles import router as profiles_router
from app.api.routes.matching import router as matching_router

app = FastAPI(
    title="Busca-Freelaí",
    description="Sistema de recomendação de projetos da Workana baseado em compatibilidade profissional.",
    version="0.1.0",
)

app.include_router(profiles_router)
app.include_router(matching_router)