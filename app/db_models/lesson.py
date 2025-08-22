from sqlalchemy import Integer, String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base
from dataclasses import dataclass

@dataclass
class Lesson(Base):
    __tablename__ = "lesson"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    book:Mapped[str] = mapped_column(String, nullable=False)
    chapter:Mapped[int] = mapped_column(Integer, nullable=False)
    verse_start:Mapped[int] = mapped_column(Integer, nullable=False)
    verse_end:Mapped[int] = mapped_column(Integer, nullable=False)
    passage:Mapped[str] = mapped_column(Text, nullable=False)
    context:Mapped[str] = mapped_column(Text, nullable=False)
    themes:Mapped[str] = mapped_column(Text, nullable=False)
    reflection:Mapped[str] = mapped_column(Text, nullable=False)
    model_used:Mapped[str] = mapped_column(String)
    created_at:Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
