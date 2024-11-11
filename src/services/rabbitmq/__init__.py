import pika


class RabbitMQ:
    
    def connection(self):                
        try:
            return pika.BlockingConnection(pika.ConnectionParameters(
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
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host="127.0.0.1", 
                port=5672, 
                credentials=pika.PlainCredentials(username="leii", password="kn00b"),
                virtual_host="jublia"
            ))
            
            ch = connection.channel()
            ch.queue_declare("email_broadcast", durable=True)
            
            connection.close()
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error when try to initialize queue, got: {e}")
    