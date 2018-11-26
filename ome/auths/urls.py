from django.urls import path
from .views import register,user_login

urlpatterns = [
    path("register/", register, name="register"),
    path("user-login/", user_login, name="user-login"),

]
