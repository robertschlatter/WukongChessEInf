
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
