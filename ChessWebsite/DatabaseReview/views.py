from random import randint

from django.shortcuts import render, redirect, get_object_or_404
from .forms import FileUploadForm
from .models import ChessGameFile
from django.http import JsonResponse

def databaseReviewView(request):
    randomNum = randint(0,10000000)
    files = ChessGameFile.objects.all()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('databaseReviewView')
    else:
        form = FileUploadForm()
    return render(request, 'DatabaseReview/wukong_chessboardjs.html', {'form': form,'files': files,'randomNum' : randomNum})

def deleteFileView(request, pk):
    file = get_object_or_404(ChessGameFile, pk=pk)
    file.delete()
    return redirect('databaseReviewView')
