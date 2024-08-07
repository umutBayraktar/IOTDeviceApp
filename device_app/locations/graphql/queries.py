import graphene

from locations.models import Location
from locations.graphql.types import LocationType


class Query(graphene.ObjectType):
    location_history_by_device = graphene.List(LocationType, device_name=graphene.String(required=True))
    last_locations_for_all_devices = graphene.List(LocationType)

    def resolve_location_history_by_device(self, info, device_name):
        return Location.objects.filter(device__name=device_name).order_by('-timestamp')

    def resolve_last_locations_for_all_devices(self, info):
        return Location.objects.all().order_by('device_id', '-timestamp').distinct('device_id')