from manage import init_django


init_django()
from django.conf import settings
from location_consumer.services import RabbitMQService
from location_consumer.tasks import create_location




if __name__ == '__main__':
    rabbitmq_service = RabbitMQService(
        host=settings.RABBITMQ_HOST,
        port=settings.RABBITMQ_PORT,
        username=settings.RABBITMQ_USER,
        password=settings.RABBITMQ_PASSWORD,
        vhost=settings.RABBITMQ_VIRTUALHOST
    )
    queue_name = settings.QUEUE_NAME
    rabbitmq_service.set_consuming_task(queue_name, callback=create_location)
    rabbitmq_service.start_consume()
