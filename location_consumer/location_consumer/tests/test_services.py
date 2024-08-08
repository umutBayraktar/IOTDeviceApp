from django.test import TestCase
from unittest.mock import patch, MagicMock
from location_consumer.services import RabbitMQService


class TestRabbitMQService(TestCase):
    def setUp(self):
        self.rabbitmq_service = RabbitMQService('localhost', 5672, 'guest', 'guest')

    @patch('pika.BlockingConnection')
    def test_connect(self, mock_connection):
        self.rabbitmq_service.connect()
        mock_connection.assert_called_once()

    @patch('pika.BlockingConnection')
    def test_disconnect(self, mock_connection):
        self.rabbitmq_service.connection = mock_connection
        self.rabbitmq_service.disconnect()
        mock_connection.close.assert_called_once()

    @patch('pika.BlockingConnection')
    def test_send_data(self, mock_connection):
        self.rabbitmq_service.connection = mock_connection
        self.rabbitmq_service.channel = MagicMock()
        with self.assertRaises(ValueError):
            self.rabbitmq_service.send_data('test_queue', 'data')

    @patch('pika.BlockingConnection')
    def test_set_consuming_task(self, mock_connection):
        self.rabbitmq_service.connection = mock_connection
        self.rabbitmq_service.channel = MagicMock()
        self.rabbitmq_service.set_consuming_task('test_queue', lambda x: x)
        self.rabbitmq_service.channel.basic_consume.assert_called_once()

    @patch('pika.BlockingConnection')
    def test_start_consume(self, mock_connection):
        self.rabbitmq_service.connection = mock_connection
        self.rabbitmq_service.channel = MagicMock()
        self.rabbitmq_service.start_consume()
        self.rabbitmq_service.channel.start_consuming.assert_called_once()