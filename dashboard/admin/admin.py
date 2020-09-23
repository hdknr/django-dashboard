from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from corebase.admin import default_list_display, TreeModelAdmin
from . import inlines
from .. import models


@admin.register(models.Topic)
class TopicAdmin(TreeModelAdmin):
    list_display = [
        "title",
        "full_code_path",
        "id",
        "tree_id",
    ]
    list_filter = []
    search_fields = [
        "code",
        "title",
    ]
    exclude = ["created_at"]
    mptt_level_indent = 30
    mptt_indent_field = "title"


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = default_list_display(
        models.Message,
    )
    raw_id_fields = ["topic"]
    search_fields = []
    exclude = ["created_at"]


@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = default_list_display(
        models.Notice,
    )
    list_filter = [
        "read",
    ]
    raw_id_fields = ["message", "user"]
    search_fields = [
        "user__username",
        "notice__subject",
        "notice__message",
    ]
    exclude = ["created_at"]
