import pika
from src.config import Config


class RabbitMQ:
    def __init__(self):
        self.config = Config()

    def connection(self):
        try:
            return pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=self.config.RABBITMQ_HOST,
                    port=self.config.RABBITMQ_PORT,
                    credentials=pika.PlainCredentials(
                        username=self.config.RABBITMQ_USER,
                        password=self.config.RABBITMQ_PASSWORD,
                    ),
                    virtual_host=self.config.RABBITMQ_VHOST,
                )
            )
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error when try to initialize connection, got: {e}")

        return None

    def init_queue(self):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=self.config.RABBITMQ_HOST,
                    port=self.config.RABBITMQ_PORT,
                    credentials=pika.PlainCredentials(
                        username=self.config.RABBITMQ_USER,
                        password=self.config.RABBITMQ_PASSWORD,
                    ),
                    virtual_host=self.config.RABBITMQ_VHOST,
                )
            )

            ch = connection.channel()
            ch.exchange_declare(exchange="email_broadcast_exchange", durable=True)
            ch.queue_declare("email_broadcast_queue", durable=True)
            ch.queue_bind(
                exchange="email_broadcast_exchange",
                queue="email_broadcast_queue",
                routing_key="email_broadcast_route",
            )
            connection.close()

        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error when try to initialize queue, got: {e}")
