#This is the urls.py file for a Django project.
# It defines the URL patterns for the user authentication views, userLoginView, userSignUpView, and userLogoutView, which are imported from the views.py module.
# The urlpatterns list maps the URLs to their corresponding views and assigns them names for easy reference in other parts of the project.
# This file is important because it serves as a routing mechanism for incoming requests, ensuring that each request is directed to the appropriate view to handle it.




# Import necessary modules
from django.urls import path
from .views import userLoginView, userSignUpView, userLogoutView

# Define the urlpatterns list with paths to views
urlpatterns = [
    # Route the login view to /login with the name 'UserAdministrationLoginView'
    path('login',userLoginView, name='UserAdministrationLoginView'),
    # Route the sign-up view to /signUp with the name 'UserAdministrationSignUpView'
    path('signUp',userSignUpView, name='UserAdministrationSignUpView'),
    # Route the logout view to /logout with the name 'UserAdministrationLogoutView'
    path('logout',userLogoutView, name='UserAdministrationLogoutView')
]
