from src.services.rabbitmq import RabbitMQ
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import BasicProperties, Basic

def main():
    rabbitmq = RabbitMQ()
    
    ch = rabbitmq.connection().channel()
    
    ch.basic_qos(prefetch_count=1)
    ch.basic_consume(queue='email_broadcast_queue', on_message_callback=send_email)
    ch.start_consuming()
    
    
def send_email(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
    print(" Received %s" % body.decode())
    print(" Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)