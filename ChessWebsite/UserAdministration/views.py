#The views.py file in a Django project contains the view functions that handle HTTP requests and return HTTP responses.
# This file is an essential part of any Django project as it defines how data is presented to users and how users interact with the system.
# In this specific views.py file, there are three views defined: userLoginView, userSignUpView, and userLogoutView.
# The userLoginView handles user authentication, userSignUpView handles user registration, and userLogoutView handles user log out.
from random import randint

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# View for user login
def userLoginView(request):
    randomNum = randint(0, 10000000)
    # Create an instance of the AuthenticationForm
    loginForm = AuthenticationForm()

    if request.method == 'POST':
        # If the request method is POST, create an instance of the AuthenticationForm with the POST data
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            # If the form data is valid, retrieve the username and password from the cleaned data
            username = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')
            # Authenticate the user with the retrieved username and password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # If the user is authenticated, log the user in and redirect them to the startScreenLobbyView
                login(request, user)
                return redirect('startScreenLobbyView')  # Replace 'home' with the name of your homepage URL pattern
            else:
                # If the user is not authenticated, add an error to the form
                loginForm.add_error(None, 'Invalid username or password')
    else:
        # If the request method is not POST, create an instance of the AuthenticationForm
        loginForm = AuthenticationForm(request)
    # Render the userLogin.html template with the loginForm instance
    return render(request, 'UserAdministration/userLogin.html', {'loginForm': loginForm,'randomNum' : randomNum})


# View for user signup
def userSignUpView(request):
    randomNum = randint(0, 10000000)
    # Create an instance of the UserCreationForm
    registerForm = UserCreationForm()

    if request.method == 'POST':
        # If the request method is POST, create an instance of the UserCreationForm with the POST data
        registerForm = UserCreationForm(request.POST)
        if registerForm.is_valid():
            # If the form data is valid, save the new user
            registerForm.save()
            # Redirect the user to the login page
            return redirect('UserAdministrationLoginView')

    # Render the userSignUp.html template with the registerForm instance
    context = {'registerForm' : registerForm,'randomNum' : randomNum}
    return render(request, 'UserAdministration/userSignUp.html', context)


# View for user logout
def userLogoutView(request):
    randomNum = randint(0, 10000000)
    # Log the user out
    logout(request)
    # Redirect the user to the startScreenLobbyView
    return redirect('startScreenLobbyView')
