from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from src.models import Base

class EmailBroadcast(Base):
    __tablename__ = 'email_broadcasts'

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(150), nullable=False)
    body: Mapped[str] = mapped_column(Text(), nullable=False)
    scheduled_at: Mapped[str] = mapped_column(DateTime(), nullable=False)
    
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))

    def __init__(self, subject, body, scheduled_at, event_id):
        self.subject = subject
        self.body = body
        self.scheduled_at = scheduled_at
        self.event_id = event_id