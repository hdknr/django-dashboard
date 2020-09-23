import channels_graphql_ws
import graphene
from logging import getLogger
from .query import Notice
from dashboard import models

logger = getLogger()


class LatestNotice(channels_graphql_ws.Subscription):
    # Subscription payload.
    title = graphene.String()
    notices = graphene.List(Notice)

    class Arguments:
        """That is how subscription arguments are defined."""
        # TODO
        arg1 = graphene.String()
        arg2 = graphene.String()

    @staticmethod
    def subscribe(root, info, arg1, arg2):
        """Called when user subscribes."""
        # logger.debug(f'LatestPost.subscribe {root} {info} {arg1} {arg2}')
        # Return the list of subscription group names.
        if hasattr(info.context, 'user') and info.context.user.is_authenticated:
            return info.context.user.subscription_groups
        return ['*']

    @staticmethod
    def publish(payload, info, arg1, arg2):
        """Called to notify the client."""
        logger.debug(f'LatestPost.publish {payload} {info} {arg1} {arg2}')

        # Here `payload` contains the `payload` from the `broadcast()`
        # invocation (see below). You can return `MySubscription.SKIP`
        # if you wish to suppress the notification to a particular
        # client. For example, this allows to avoid notifications for
        # the actions made by this particular client.
        if hasattr(info.context, 'user') and info.context.user.is_authenticated:
            # TODO: 特定ユーザー向け未読
            return LatestNotice(title='Latest Notices', notices=models.Notice.objects.all())

        # TODO: 全員対象
        return LatestNotice(title='Latest Notices', notices=models.Notice.objects.all())


class Subscription(graphene.ObjectType):
    """Root GraphQL subscription."""
    latestnotice = LatestNotice.Field()
