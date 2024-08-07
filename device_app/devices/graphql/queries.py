import graphene
from devices.models import Device
from devices.graphql.types import DeviceType


class Query(graphene.ObjectType):
    all_devices = graphene.List(DeviceType)
    device_by_id = graphene.Field(DeviceType, id=graphene.ID(required=True))

    def resolve_all_devices(self, info):
        return Device.objects.all()

    def resolve_device_by_id(self, info, id):
        return Device.objects.get(pk=id)
