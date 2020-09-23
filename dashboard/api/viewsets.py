from rest_framework import viewsets
from apibase import paginations
from . import serializers, filters, permissions
from .. import models


class TopicViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.Permission, ]
    filter_class = filters.TopicFilter
    serializer_class = serializers.TopicSerializer
    queryset = models.Topic.objects.all()
    pagination_class = paginations.Pagination


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.Permission, ]
    filter_class = filters.MessageFilter
    serializer_class = serializers.MessageSerializer
    queryset = models.Message.objects.all()
    pagination_class = paginations.Pagination


class NoticeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.Permission, ]
    filter_class = filters.NoticeFilter
    serializer_class = serializers.NoticeSerializer
    queryset = models.Notice.objects.all()
    pagination_class = paginations.Pagination
