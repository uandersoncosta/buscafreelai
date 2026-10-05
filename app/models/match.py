from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import Base

class Match(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    profile_id: Mapped[int] = mapped_column(
        ForeignKey("profiles.id"),
        nullable=False,
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
    )

    score: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    analise: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )