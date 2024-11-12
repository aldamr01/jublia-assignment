from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.models import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(Integer(), nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    def __init__(self, name=None, email=None) -> None:
        self.name = name
        self.email = email

    def __repr__(self) -> None:
        return f"<User {self.name!r}>"
