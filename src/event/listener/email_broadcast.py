import threading, json, smtplib

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import BasicProperties, Basic
from sqlalchemy.orm import sessionmaker

from src.services.email import Mail
from src.services.database import engine
from src.services.rabbitmq import RabbitMQ
from src.models.email_broadcast import EmailBroadcast


def main():
    thread = threading.Thread(target=consumer)
    thread.daemon = True
    thread.start()


def consumer():
    rabbitmq = RabbitMQ()

    ch = rabbitmq.connection().channel()

    ch.basic_qos(prefetch_count=1)
    ch.basic_consume(queue="email_broadcast_queue", on_message_callback=send_email)
    ch.start_consuming()


def send_email(
    ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes
):
    print(" Received %s" % body.decode())
    decoded_body = body.decode()
    mail = Mail()

    try:
        decoded_json = json.loads(decoded_body)

        email = decoded_json.get("email")
        broadcast_id = decoded_json.get("broadcast_id")

        session = sessionmaker(bind=engine)
        s = session()
        mail_connection = mail.connection()

        broadcast = (
            s.query(EmailBroadcast).where(EmailBroadcast.id == broadcast_id).one()
        )
        recepients = [email]

        print(f" Subject: broadcast.subject, to recepient: {email}")
        mail.sendmail(
            mail_connection,
            broadcast.subject,
            broadcast.body,
            email,
            "testing@test.com",
        )
        print("Email sent.")

    except Exception as e:
        print(f"Error, got: {e}")

    print(" Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
