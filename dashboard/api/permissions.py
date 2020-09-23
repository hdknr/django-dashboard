from apibase import permissions
from logging import getLogger

logger = getLogger("app")


class Permission(permissions.Permission):
    PERM_CODE = 'dashboard.change_notice'
    