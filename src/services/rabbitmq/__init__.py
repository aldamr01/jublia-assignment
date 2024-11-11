import pika


class RabbitMQ:
    
    def __init__(self) -> None:                
        try:
            self.connect =  pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        except pika.exceptions.AMQPConnectionError as exc:
            print(f"Error got: {exc}")
        
        return None
    