import pika
import json


class RabbitMQService:
    def __init__(self, host, port, username, password, vhost='/'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.vhost = vhost
        self.connection = None
        self.channel = None

    def connect(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host, self.port, self.vhost, credentials))
        self.channel = self.connection.channel()

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.channel = None

    def send_data(self, queue_name, data, exchange=''):
        if not isinstance(data, dict):
            raise ValueError('Data must be a dictionary')
        if not self.connection:
            self.connect()
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=queue_name,
            body=json.dumps(data),
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )
        self.disconnect()

    def set_consuming_task(self, queue_name, callback):
        if not self.connection:
            self.connect()
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_consume(
            queue=queue_name, on_message_callback=callback
        )

    def start_consume(self):
        if not self.connection:
            self.connect()
        self.channel.start_consuming()
