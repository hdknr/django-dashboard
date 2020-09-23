from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import defs


class User(defs.User):

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    @property
    def subscription_groups(self):
        return [self.private_group, '*']

    @property
    def private_group(self):
        return f'user-{self.id}'
