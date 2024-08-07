import graphene
from devices.graphql.queries import Query as devices_query
from devices.graphql.mutations import Mutation as devices_mutation

from locations.graphql.queries import Query as locations_query
from locations.graphql.mutations import Mutation as locations_mutation


class Query(devices_query, locations_query, graphene.ObjectType):
    pass


class Mutation(devices_mutation, locations_mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
