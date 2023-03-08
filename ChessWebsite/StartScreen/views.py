from django.shortcuts import render  # Import the render function to return an HTML template response

# Define the view function to handle the request
def startScreenLobbyView(requests):
    # Define an empty context dictionary
    context = {}
    # Render the HTML template 'StartScreen/startScreenLobby.html' with the empty context dictionary as a parameter
    # and return the resulting HTML as the response to the request
    return render(requests, 'StartScreen/startScreenLobby.html', context)
