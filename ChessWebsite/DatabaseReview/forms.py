from django import forms
from .models import ChessGameFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = ChessGameFile
        fields = ('title', 'file',)