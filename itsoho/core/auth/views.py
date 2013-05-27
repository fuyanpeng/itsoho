# -*- coding -*-
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout
from itsoho.core.auth.models import Xuser as User
from itsoho.core.auth.forms import LoginForm, RegisterForm

def login(request):

    if request.method == "POST":
        next_url = request.REQUEST.get('next','')
        form = LoginForm(data=request.POST)
        if form.is_valid():
            django_login(request, form.get_user())
            return redirect(next_url or 'home')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html',{
        'form': form,
    })

def logout(request):
    django_logout(request)
    return redirect('home')

def register(request):

    if request.method == "POST":
        data = request.POST
        form = RegisterForm(data=data)
        if form.is_valid():
            user = User.objects.create_user(username=data["username"],
                                            email=data["email"],
                                            password=data["password"]
                                        )
            user.save()

    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {
        'form': form,
    })
