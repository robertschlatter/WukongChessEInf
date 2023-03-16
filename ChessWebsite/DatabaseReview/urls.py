from django.urls import path
from .views import databaseReviewView, deleteFileView # Import the view function to be used for the URL

urlpatterns = [
    path('', databaseReviewView, name='databaseReviewView'),
    path('file/<int:pk>/delete/', deleteFileView, name='deleteFileView')
]
