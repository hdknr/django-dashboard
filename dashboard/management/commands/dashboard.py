from django.contrib.auth import get_user_model
from dashboard.channel.consumers import ChatConsumer, NoticeConsumer
import djclick as click
from logging import getLogger
log = getLogger()


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.argument('group_name')
@click.argument('message')
@click.pass_context
def send_chat(ctx, group_name, message):
    '''Offline Send'''
    ChatConsumer.from_offline(group_name, message)


@main.command()
@click.argument('user')
@click.argument('message')
@click.pass_context
def send_notice(ctx, user, message):
    '''Offline Send'''
    if user.isdigit():
        user = get_user_model().objects.filter(id=int(user)).first()
    else:
        user = get_user_model().objects.filter(username=user).first()

    if user:
        NoticeConsumer.from_offline(user, message)
