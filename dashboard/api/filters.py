'''
https://django-filter.readthedocs.io/en/master/
'''
from apibase.filters import BaseFilter
from .. import models


class TopicFilter(BaseFilter):

    class Meta:
        model = models.Topic
        exclude = ['']


class MessageFilter(BaseFilter):

    class Meta:
        model = models.Message
        exclude = ['']

class NoticeFilter(BaseFilter):

    class Meta:
        model = models.Notice
        exclude = ['']
