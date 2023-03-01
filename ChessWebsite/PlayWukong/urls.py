from django.urls import path
from .views import playWukongView

urlpatterns = [
    path('<int:ID>',playWukongView, name='playWukongView'),
]
