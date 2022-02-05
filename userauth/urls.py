from django.urls import path
from .views import Login, register, Home, Logout
urlpatterns = [
    path('Login', Login, name="Login"),
    path('register', register, name="register"),
    path('',Home),
    path('Logout',Logout, name="Logout")
]