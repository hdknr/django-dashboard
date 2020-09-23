from django.dispatch import receiver
from django.db.models.signals import post_save
from . import models
from .api.schema.subscription import LatestNotice

from logging import getLogger
logger = getLogger()


@receiver(post_save, sender=models.Notice)
def on_notice_saved(sender, instance, created=False, **kwargs):
    '''Notic:post_save'''
    if instance and created:
        if instance.user:
            print(instance.user.private_group, instance.message.subject)
            LatestNotice.broadcast(
                group=instance.user.private_group,
                payload={'title': instance.message.subject})
