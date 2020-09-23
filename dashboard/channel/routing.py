from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('dashboard/ws/notice/', consumers.NoticeConsumer),
    path('dashboard/ws/chat/<str:room_name>/', consumers.ChatConsumer),
]
