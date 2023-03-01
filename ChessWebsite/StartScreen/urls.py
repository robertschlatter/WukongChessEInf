from django.urls import path
from .views import startScreenLobbyView

urlpatterns = [
    path('',startScreenLobbyView, name='startScreenLobbyView'),
]