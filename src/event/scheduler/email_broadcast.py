import json

from datetime import datetime
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import BasicProperties

from sqlalchemy.orm import sessionmaker

from src.models.email_broadcast import EmailBroadcast
from src.models.user import User
from src.services.database import engine
from src.services.rabbitmq import RabbitMQ


def main():
    s = sessionmaker(bind=engine)
    c = RabbitMQ()
    cn = c.connection
    ch = cn.channel()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    broadcasts = s().query(EmailBroadcast).where(EmailBroadcast.scheduled_at==current_time)
    users = s().query(User).all()
    
    s().close

    for broadcast in broadcasts:
        bsubject = broadcast.subject
        
        for user in users:
            email = user.email
            
            queue_email(user.email, broadcast.id, ch)
            print(f"Queue for broadcast {bsubject} to user: {email}")
        
    ch.close()
    
def queue_email(user_email, broadcast_id, channel: BlockingChannel):
    body = json.dumps({
            "email": user_email,
            "broadcast_id": broadcast_id
        }).encode('utf-8')
    
    channel.basic_publish(
        exchange='email_broadcast_exchange',
        routing_key='email_broadcast_route',
        body=body,
        properties=BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )