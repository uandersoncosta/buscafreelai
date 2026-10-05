from sqlalchemy import JSON, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255))

    url: Mapped[str] = mapped_column(String(500),unique=True,nullable=False,)

    conteudo: Mapped[str] = mapped_column(Text)

    qnt_propostas: Mapped[int | None] = mapped_column(Integer,nullable=True,)

    valor: Mapped[str | None] = mapped_column(String(100),nullable=True,)

    skills: Mapped[list] = mapped_column(JSON)

    analise: Mapped[str | None] = mapped_column(Text,nullable=True,)