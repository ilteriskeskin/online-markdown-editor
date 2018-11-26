from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


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


def register(request):
    form = RegisterForm(data=request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Tebrikler Kayıt İlemi Başarılı', extra_tags='success')
                return HttpResponseRedirect(reverse('markdown-create'))

    return render(request, 'auths/register.html', context={'form': form})
