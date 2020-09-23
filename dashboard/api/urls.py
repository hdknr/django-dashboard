from django.urls import path, include
from apibase.routers import DefaultRouter
from . import viewsets


router = DefaultRouter(root_view_name='api-dashboard-root')
router.register(r'topic', viewsets.TopicViewSet)
router.register(r'message', viewsets.MessageViewSet)
router.register(r'notice', viewsets.NoticeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
