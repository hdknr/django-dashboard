from django.urls import path
from . import views


urlpatterns = [
    path('chat/graphql/', views.chat_graphql, name='dashboard_chat_graphql'),
    path('chat/<str:room_name>/', views.chat_room, name='dashboard_chat_room'),
    path('chat/', views.chat_index, name='dashboard_chat_index'),
    path('', views.notice_index, name='dashboard_notice_index'),
]
