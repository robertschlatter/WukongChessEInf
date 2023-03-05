from django.urls import path
from .views import userLoginView, userSignUpView, userLogoutView

urlpatterns = [
    path('login',userLoginView, name='UserAdministrationLoginView'),
    path('signUp',userSignUpView, name='UserAdministrationSignUpView'),
    path('logout',userLogoutView, name='UserAdministrationLogoutView')

]