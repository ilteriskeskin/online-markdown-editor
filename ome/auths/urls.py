from django.urls import path
from .views import register, user_login, user_logout, user_profile

urlpatterns = [
    path("register/", register, name="register"),
    path("user-login/", user_login, name="user-login"),
    path("user-logout/", user_logout, name="user-logout"),
    path("<slug:username>/", user_profile, name="user-profile"),

]
