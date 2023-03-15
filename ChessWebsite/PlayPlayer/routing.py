# chat/routing.py
from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path(r"playPlayer/(?P<ID>\w+)/$", consumer.ChatConsumer.as_asgi()),
]