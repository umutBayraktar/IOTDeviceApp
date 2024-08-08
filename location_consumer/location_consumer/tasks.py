import json
from devices.models import Device
from locations.models import Location
from django.db import transaction


@transaction.atomic
def create_location(ch, method, properties, body):
    data = json.loads(body)
    device_name = data.get('device')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    timestamp = data.get('timestamp')
    device = Device.objects.filter(name=device_name).first()
    if not device:
        ch.basic_ack(delivery_tag=method.delivery_tag)
    Location.objects.create(
        device=device,
        latitude=latitude,
        longitude=longitude,
        timestamp=timestamp
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)
