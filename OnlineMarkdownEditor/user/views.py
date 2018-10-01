from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register(request):
    form = RegisterForm()
    context = {
        "form":form

    }

    return render(request,"register.html",context)

def login(request):
    pass
def logout(request):
    pass