from decouple import config


def init_django():
    import django
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        SECRET_KEY=config('SECRET_KEY'),
        RABBITMQ_HOST=config('RABBITMQ_HOST', default='localhost'),
        RABBITMQ_VIRTUALHOST=config('RABBITMQ_VIRTUALHOST', default='/'),
        RABBITMQ_PORT=config('RABBITMQ_PORT', default='5672'),
        RABBITMQ_USER=config('RABBITMQ_USER', default='guest'),
        RABBITMQ_PASSWORD=config('RABBITMQ_PASSWORD', default='guest'),
        QUEUE_NAME=config('QUEUE_NAME', default='locations'),
        DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'devices',
            'locations',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': config('DB_NAME'),
                'USER': config('DB_USER', default='postgres'),
                'PASSWORD': config('DB_PASSWORD', default='postgres'),
                'HOST': config('DB_HOST', default='localhost'),
                'PORT': config('DB_PORT', default='5432')
            }
        },
        ALLOWED_HOSTS=['*'],
        DEBUG=config('DEBUG', default=False, cast=bool),
    )
    django.setup()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    init_django()
    execute_from_command_line()
