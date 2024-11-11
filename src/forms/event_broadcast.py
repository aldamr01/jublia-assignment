from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField, TextAreaField, DateTimeField
from wtforms.widgets import TextInput, Select
from sqlalchemy.orm import sessionmaker

from src.models.event import Event
from src.services.database import engine



class CreateForm(Form):    
    subject = StringField('Subject', [validators.Length(min=1, max=35)])
    body = TextAreaField('Content', [validators.Length(min=1)])
    schedule_at = StringField(
        'Schedule Time',
        id="email-schedule"
    )
    
    def __init__(self, username, *args, **kwargs):        
        super(CreateForm, self).__init__(*args, **kwargs)
        
        session = sessionmaker(bind=engine)
        events = session().query(Event).all()
        event_data = [(e.id, e.name) for e in events]
        session().close()        
        
        self.event = SelectField(
            'Event', 
            [validators.DataRequired()], 
            choices=event_data,
            id="email-event"
        )