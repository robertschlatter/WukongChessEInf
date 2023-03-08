from django.urls import path
from .views import playWukongView  # Import the view function to be used for the URL

urlpatterns = [
    # Define the URL pattern for a player's ID. The ID is passed as an integer argument to the view function.
    # The view function is playWukongView, which will handle the request and return a response.
    # The name 'playWukongView' is used to identify this URL pattern and can be referred to elsewhere in the Django application.
    path('<int:ID>', playWukongView, name='playWukongView'),
]
