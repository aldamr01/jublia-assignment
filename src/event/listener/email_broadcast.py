from src.services.rabbitmq import RabbitMQ
# from src.services.email import mail
from src.services.database import engine
from src.models.email_broadcast import EmailBroadcast

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import BasicProperties, Basic
from sqlalchemy.orm import sessionmaker


def main():
    rabbitmq = RabbitMQ()
    
    ch = rabbitmq.connection().channel()
    
    ch.basic_qos(prefetch_count=1)
    ch.basic_consume(queue='email_broadcast_queue', on_message_callback=send_email)
    ch.start_consuming()
    
    
def send_email(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
    print(" Received %s" % body.decode())
    
    # msg = body.decode()
    # session = sessionmaker(bind=engine)
    # s = session()
    
    # broadcast = s.query(EmailBroadcast).where(EmailBroadcast.id==msg['broadcast_id']).one()
    # recepients = [msg['email']]
    
    # mail.send_message(broadcast.subject, recepients, broadcast.body)
    
    print(" Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)