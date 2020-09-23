from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from . import defs

User = get_user_model()


class Topic(defs.Topic):

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')
        constraints = [
            models.UniqueConstraint(fields=['tree_id', 'level', 'code'], name='unique_code'),
        ]

    def __str__(self):
        return self.full_title


class Message(defs.Message):
    topic = models.ForeignKey(
        Topic, verbose_name=_('Topic'),
        null=True, default=None, blank=True,
        on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def __str__(self):
        return self.subject


class Notice(defs.Notice):
    message = models.ForeignKey(
        Message, verbose_name=_('Message'),
        null=True, default=None, blank=True,
        on_delete=models.SET_DEFAULT)
    
    user = models.ForeignKey(
        User, verbose_name=_('User'),
        null=True, default=None, blank=True,
        on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name = _('Notice')
        verbose_name_plural = _('Notices')
        constraints = [
            models.UniqueConstraint(fields=['message', 'user'], name='unique_recipient'),
        ]
        ordering = [
            'read',
            '-created_at', 
            'user',
        ]

    def __str__(self):
        return f"{self.message} ({self.user})"

