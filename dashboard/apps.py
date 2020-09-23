from django import apps
from django.utils.translation import ugettext_lazy as _


class AppConfig(apps.AppConfig):
    name = 'dashboard'
    verbose_name = _('Dashboard')

    def ready(self):
        from . import tasks
