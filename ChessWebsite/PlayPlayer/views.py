from django.shortcuts import render

# Create your views here.
def playPlayerView(requests,ID):
    context = {'ID' : ID}
    return render(requests,'PlayPlayer/wukong_chessboardjs.html',context)