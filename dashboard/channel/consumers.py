from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async as DBASYNC
from channels.layers import get_channel_layer
from channels.exceptions import DenyConnection

from asgiref.sync import async_to_sync
import json
from logging import getLogger
logger = getLogger()


class ChatConsumer(AsyncWebsocketConsumer):
    @classmethod
    def get_room_group_name(cls, name):
        return f"chat_{name}"

    @property
    def current_user(self):
        return self.scope['user']

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = self.get_room_group_name(self.room_name)
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        logger.debug(f'ChatConsumer.receive: User = {self.current_user}') 
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    @classmethod
    def from_offline(cls, group_name, message):
        channel_group_name = cls.get_room_group_name(group_name)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            channel_group_name, {"type": "chat_message", "message": message}
        )



class NoticeConsumer(AsyncWebsocketConsumer):
    PERM_CODE = 'dashboard.change_notice'
    EVENT = 'dashboard_notice'

    @property
    def current_user(self):
        return self.scope['user']

    @classmethod
    def get_group_name(self, user):
        return f"notice_{user.username}"

    async def connect(self):
        if not await DBASYNC(self.current_user.has_perm)(self.PERM_CODE):
            logger.debug(f'{self.current_user} has no permission.({self.PERM_CODE})')
            raise DenyConnection('permission error')

        self.group_name = self.get_group_name(self.current_user)

        # Join room group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        if not self.current_user.is_staff:
            # do nothing 
            return

        logger.debug(f'ChatConsumer.receive: User = {self.current_user}') 
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": self.EVENT, "message": message}
        )

    # Receive message from room group
    async def dashboard_notice(self, event):
        message = event["message"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    @classmethod
    def from_offline(cls, user, message):
        channel_layer = get_channel_layer()
        channel_group_name = cls.get_group_name(user)
        async_to_sync(channel_layer.group_send)(
            channel_group_name, {"type": cls.EVENT, "message": message}
        )
