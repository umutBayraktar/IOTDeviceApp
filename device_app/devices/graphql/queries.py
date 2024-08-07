import graphene
from devices.models import Device
from devices.graphql.types import DeviceType


class Query(graphene.ObjectType):
    all_devices = graphene.List(DeviceType)
    device_by_name = graphene.Field(DeviceType, name=graphene.String(required=True))

    def resolve_all_devices(self, info):
        return Device.objects.all()

    def resolve_device_by_name(self, info, name):
        return Device.objects.get(name=name)
