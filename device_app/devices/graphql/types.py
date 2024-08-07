from graphene_django import DjangoObjectType
from devices.models import Device


class DeviceType(DjangoObjectType):
    class Meta:
        model = Device
