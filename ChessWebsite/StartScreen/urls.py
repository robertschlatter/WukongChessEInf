from django.urls import path
from .views import startScreenLobbyView  # Import the view function to be used for the URL

urlpatterns = [
    # Define the URL pattern for an empty URL (i.e., the root URL).
    # The view function is startScreenLobbyView, which will handle the request and return a response.
    # The name 'startScreenLobbyView' is used to identify this URL pattern and can be referred to elsewhere in the Django application.
    path('', startScreenLobbyView, name='startScreenLobbyView'),
]
