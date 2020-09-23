from graphene_django.views import GraphQLView
from django.urls import path, include
from apibase.views import sdl
from . import views, schema


urlpatterns = [
    path("graphql/sdl", sdl),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    path("", views.index),
]


websocket_urlpatterns = [
    path("ws/graphql/", schema.consumer),
]
