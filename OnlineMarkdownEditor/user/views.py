from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as dj_login
from django.contrib import messages

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        dj_login(request,newUser)
        messages.info(request,"Başarıyla Kayıt Oldunuz...")

        return render(request,"index.html")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)
def login(request):

    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        dj_login(request,user)
        return render(request,"index.html")
    return render(request,"login.html",context)
    
def logout(request):
    pass