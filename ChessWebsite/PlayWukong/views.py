from random import randint

from django.shortcuts import render, redirect  # Import the render function to return an HTML template response
from DatabaseReview.forms import FileUploadForm
from DatabaseReview.models import ChessGameFile

# Define the view function to handle the request
def playWukongView(request, ID):
    randomNum = randint(0, 10000000)
    files = ChessGameFile.objects.all()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('playPlayerView')
    else:
        form = FileUploadForm()
    return render(request, 'PlayWukong/wukong_chessboardjs.html', {'form': form,'files': files, 'ID':ID,'randomNum' : randomNum})

