from graphene_django import DjangoObjectType
from locations.models import Location


class LocationType(DjangoObjectType):
    class Meta:
        model = Location
