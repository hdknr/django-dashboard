from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json


def chat_index(request):
    return render(request, 'dashboard/chat/index.html', {})


def chat_graphql(request):
    return render(request, 'dashboard/chat/graphql.html', {})


def chat_room(request, room_name):
    return render(request, 'dashboard/chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def notice_index(request):
    return render(request, 'dashboard/notice/index.html', {})
