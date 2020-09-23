import graphene
from dashboard.api import schema as dashboard_schema

from apibase.consumers import create_schema_consumer


class Query(dashboard_schema.Query, graphene.ObjectType):
    pass


class Mutation(dashboard_schema.Mutation, graphene.ObjectType):
    pass


class Subscription(dashboard_schema.Subscription, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
    # mutation=Mutation,
    subscription=Subscription,
    auto_camelcase=False,
)


consumer = create_schema_consumer(schema, name="SampleWsConsumer")
