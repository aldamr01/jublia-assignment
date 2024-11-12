from wtforms import Form, StringField, validators, SelectField, TextAreaField
from sqlalchemy.orm import sessionmaker

from src.models.event import Event
from src.services.database import engine


class CreateForm(Form):
    event = SelectField(
        "Event", [validators.DataRequired()], choices=[], id="email-event"
    )
    subject = StringField("Subject", [validators.Length(min=1, max=35)])
    body = TextAreaField("Content", [validators.Length(min=1)])
    schedule_at = StringField("Schedule Time", [validators.DataRequired()], id="email-schedule")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        session = sessionmaker(bind=engine)()
        try:
            events = session.query(Event).all()
            self.event.choices = [(e.id, e.name) for e in events]
        finally:
            session.close()