import graphene
from graphene_django.types import DjangoObjectType
from apibase.schema import NodeMixin, NodeSet
from dashboard import models
from dashboard.api import filters


class Topic(NodeMixin, DjangoObjectType):
    full_code_path = graphene.String()

    class Meta:
        model = models.Topic
        filterset_class = filters.TopicFilter
        interfaces = (graphene.Node, )
        convert_choices_to_enum = False


class Notice(NodeMixin, DjangoObjectType):

    class Meta:
        model = models.Notice
        filterset_class = filters.NoticeFilter
        interfaces = (graphene.Node, )
        convert_choices_to_enum = False


class Message(NodeMixin, DjangoObjectType):

    class Meta:
        model = models.Message
        filterset_class = filters.MessageFilter
        interfaces = (graphene.Node, )
        convert_choices_to_enum = False


class Query(graphene.ObjectType):
    topic = graphene.relay.Node.Field(Topic)
    topic_set = NodeSet(Topic)

    message = graphene.relay.Node.Field(Message)
    message_set = NodeSet(Message)

    notice = graphene.relay.Node.Field(Notice)
    notice_set = NodeSet(Notice)
