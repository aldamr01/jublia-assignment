from wtforms import Form, StringField, validators, SelectField, TextAreaField
from sqlalchemy.orm import sessionmaker

from src.models.event import Event
from src.services.database import engine


class CreateForm(Form):
    session = sessionmaker(bind=engine)
    events = session().query(Event).all()
    event_data = [(e.id, e.name) for e in events]
    session().close()

    event = SelectField(
        "Event", [validators.DataRequired()], choices=event_data, id="email-event"
    )
    subject = StringField("Subject", [validators.Length(min=1, max=35)])
    body = TextAreaField("Content", [validators.Length(min=1)])
    schedule_at = StringField("Schedule Time", id="email-schedule")
