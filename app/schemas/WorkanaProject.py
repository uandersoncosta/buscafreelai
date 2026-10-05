from pydantic import BaseModel, HttpUrl

class WorkanaProject(BaseModel):
  title: str
  url: HttpUrl
  conteudo: str
  qnt_propostas: int | None = None
  valor: str | None = None
  skills: list[str] = []
  analise: str | None = None