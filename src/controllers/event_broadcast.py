from flask import request, Blueprint, render_template
from sqlalchemy.orm import sessionmaker
from src.services.database import engine
from src.models.email_broadcast import EmailBroadcast
from src.forms.event_broadcast import CreateForm

event_broadcast = Blueprint("event_broadcast", __name__)

base_template = "modules/event_broadcast/"

session = sessionmaker(bind=engine)

@event_broadcast.route('/save_emails', methods=["POST", "GET"])
def save_emails():    
    f = CreateForm(request.form)
    s = session()
    
    if request.method == "POST" and f.validate():
        
        
        email_broadcast_data = EmailBroadcast(
            event_id= f.event.data,
            subject= f.subject.data,
            body= f.body.data,
            scheduled_at= f.schedule_at.data
        )
        
        try:
            s.add(email_broadcast_data)
        except Exception as e:
            s.rollback()
            print(f"Error when saving data, got: {e}")
            
        s.commit()
        
    schedules = s.query(EmailBroadcast).all()
    
    s.close()
               
    return render_template(f"{base_template}index.j2", **{
        "form": f,
        "schedules": schedules
    })
    
    
