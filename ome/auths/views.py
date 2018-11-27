from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from .models import UserProfile


def user_login(request):
    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                msg = "Merhabalar {} sisteme Hoş geldiniz".format(username)
                messages.success(request, msg, extra_tags='success')
                return HttpResponseRedirect(reverse('markdown-create'))

    return render(request, 'auths/login.html', context={'form': form})


def user_logout(request):
    username = request.user.username
    logout(request)
    msg = "Sistemden çıkış yaptınız. Güle güle {}".format(username)
    messages.success(request, msg, extra_tags='success')
    return HttpResponseRedirect(reverse('user-login'))


def register(request):
    form = RegisterForm(data=request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Tebrikler Kayıt İşlemi Başarılı {}'.format(username), extra_tags='success')
                return HttpResponseRedirect(reverse('markdown-create'))

    return render(request, 'auths/register.html', context={'form': form})


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'auths/user_profile.html', context={'user': user})
