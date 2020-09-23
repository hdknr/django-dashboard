from rest_framework import serializers
from apibase.serializers import BaseModelSerializer
from .. import models



class TopicSerializer(BaseModelSerializer):
    full_code_path = serializers.CharField(read_only=True)

    class Meta:
        model = models.Topic
        fields = '__all__'


class NoticeSerializer(BaseModelSerializer):

    class Meta:
        model = models.Notice
        fields = '__all__'


class MessageSerializer(BaseModelSerializer):

    class Meta:
        model = models.Message
        fields = '__all__'
