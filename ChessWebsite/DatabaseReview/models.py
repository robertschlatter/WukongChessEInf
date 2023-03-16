from django.db import models

# Create your models here.
class ChessGameFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='chessGameFiles/')
    uploaded_at = models.DateTimeField(auto_now_add=True)