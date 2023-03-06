from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def userLoginView(requests):
    loginForm = AuthenticationForm()

    if requests.method == 'POST':
        loginForm = AuthenticationForm(requests, requests.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')
            user = authenticate(requests, username=username, password=password)
            if user is not None:
                login(requests, user)
                return redirect('startScreenLobbyView')  # Replace 'home' with the name of your homepage URL pattern
            else:
                loginForm.add_error(None, 'Invalid username or password')
    else:
        login_form = AuthenticationForm(requests)
    return render(requests, 'UserAdministration/userLogin.html', {'loginForm': loginForm})


def userSignUpView(requests):
    registerForm = UserCreationForm()

    if requests.method == 'POST':
        registerForm = UserCreationForm(requests.POST)
        if registerForm.is_valid():
            registerForm.save()

        return redirect('UserAdministrationLoginView')

    context = {'registerForm' : registerForm}
    return render(requests, 'UserAdministration/userSignUp.html', context)

def userLogoutView(request):
    logout(request)
    return redirect('startScreenLobbyView')