from sqlalchemy import JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(100))

    skills: Mapped[list] = mapped_column(JSON)

    experiencia: Mapped[str] = mapped_column(Text)

    desired_categories: Mapped[list] = mapped_column(JSON)