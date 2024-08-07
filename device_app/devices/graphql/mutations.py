import graphene
from graphene_django import DjangoObjectType
from devices.models import Device
from devices.graphql.types import DeviceType


class CreateDevice(graphene.Mutation):
    device = graphene.Field(DeviceType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        device = Device(name=name)
        device.save()
        return CreateDevice(device=device)


class DeleteDevice(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        device = Device.objects.get(name=name)
        device.delete()
        return DeleteDevice(ok=True)


class Mutation(graphene.ObjectType):
    create_device = CreateDevice.Field()
    delete_device = DeleteDevice.Field()
