"""ChessWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Import necessary modules

from django.contrib import admin
from django.urls import path, include

#Define URL patterns

urlpatterns = [
# Admin page URL pattern
path('admin/', admin.site.urls),

# URL pattern for PlayWukong app
path('playWukong/', include('PlayWukong.urls')),

# URL pattern for PlayPlayer app
path('playPlayer/', include('PlayPlayer.urls')),

# URL pattern for StartScreen app
path('', include('StartScreen.urls')),

# URL pattern for UserAdministration app
path('user/', include('UserAdministration.urls'))
]

#Note: urlpatterns is a list of URL patterns used by Django.

#Each URL pattern maps a URL to a view that handles the request.

#The include() function is used to reference other URL pattern files within the project.