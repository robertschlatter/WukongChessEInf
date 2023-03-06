from django.urls import path
from .views import playPlayerView

urlpatterns = [
    path('<int:ID>', playPlayerView, name='playPlayerView'),
]
