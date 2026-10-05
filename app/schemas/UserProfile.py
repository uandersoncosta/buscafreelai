from pydantic import BaseModel

class UserProfile(BaseModel):
  nome: str
  skills: list[str]
  experiencia: str
  desired_categories: list[str]