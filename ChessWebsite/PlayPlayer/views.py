from django.shortcuts import render  # Import the render function to return an HTML template response

# Define the view function to handle the request
def playPlayerView(requests, ID):
    # Define a dictionary containing the player's ID as a key-value pair
    context = {'ID': ID}
    # Render the HTML template 'PlayPlayer/wukong_chessboardjs.html' with the context dictionary as a parameter
    # and return the resulting HTML as the response to the request
    return render(requests, 'PlayPlayer/wukong_chessboardjs.html', context)
