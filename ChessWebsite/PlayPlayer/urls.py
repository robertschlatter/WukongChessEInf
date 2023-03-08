from django.urls import path
from .views import playPlayerView  # Import the view function to be used for the URL

urlpatterns = [
    # Define the URL pattern for a player's ID. The ID is passed as an integer argument to the view function.
    # The view function is playPlayerView, which will handle the request and return a response.
    # The name 'playPlayerView' is used to identify this URL pattern and can be referred to elsewhere in the Django application.
    path('<int:ID>', playPlayerView, name='playPlayerView'),
]
