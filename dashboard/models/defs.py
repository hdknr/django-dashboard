from django.db import models
from django.utils.translation import ugettext_lazy as _
from corebase.models.defs import BaseModel, BaseTreeModel
from . import methods


class Topic(BaseTreeModel, methods.Topic):
    code = models.CharField(
        max_length=50,
    )

    title = models.CharField(max_length=100, null=True, blank=True, default=None)

    class Meta:
        abstract = True


class Message(BaseModel, methods.Message):
    subject = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True, default=None)
    url = models.URLField(null=True, blank=True, default=None)

    class Meta:
        abstract = True


class Notice(BaseModel, methods.Notice):

    read = models.BooleanField(
        _("Is Read"),
        default=False,
    )

    class Meta:
        abstract = True
