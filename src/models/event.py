from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from src.models import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(Integer(), nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(Text(), nullable=False)
    time: Mapped[str] = mapped_column(DateTime(), nullable=False)

    def __init__(self, name=None) -> None:
        self.name = name

    def __repr__(self) -> None:
        return f"<Event {self.name!r}>"
