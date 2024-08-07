import graphene

from locations.models import Location
from locations.graphql.types import LocationType


class Query(graphene.ObjectType):
    location_history_by_device = graphene.List(LocationType, device_id=graphene.ID(required=True))
    last_locations_for_all_devices = graphene.List(LocationType)

    def location_history_by_device(self, info, device_id):
        return Location.objects.filter(device_id=device_id).order_by('-timestamp')

    def last_locations_for_all_devices(self, info):
        return Location.objects.all().order_by('device_id', '-timestamp').distinct('device_id')