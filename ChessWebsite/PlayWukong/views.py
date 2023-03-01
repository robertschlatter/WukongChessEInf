from django.shortcuts import render

# Create your views here.
def playWukongView(requests,ID):
    context = {}
    return render(requests,'PlayWukong/wukong_chessboardjs.html',context)
