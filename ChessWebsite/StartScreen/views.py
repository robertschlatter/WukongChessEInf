from django.shortcuts import render

# Create your views here.
def startScreenLobbyView(requests):
    context = {}
    return render(requests,'StartScreen/startScreenLobby.html',context)