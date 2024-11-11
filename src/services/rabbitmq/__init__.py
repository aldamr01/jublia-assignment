import pika


class RabbitMQ:
    
    def __init__(self) -> None:                
        try:
            self.connection =  pika.BlockingConnection(pika.ConnectionParameters(
                host="127.0.0.1", 
                port=5672, 
                credentials=pika.PlainCredentials(username="leii", password="kn00b"),
                virtual_host="jublia"
            ))
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error when try to initialize connection, got: {e}")
        
        return None
    
    def init_queue(self):
        try:
            ch = self.connection.channel()
            ch.queue_declare("email_broadcast", durable=True)
            
            self.connection.close()
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error when try to initialize queue, got: {e}")
    