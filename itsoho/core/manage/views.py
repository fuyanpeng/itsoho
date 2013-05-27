# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from  itsoho.core.auth.models import Xuser, BaseInfo, EduInfo
from itsoho.core.auth.forms import BaseInfoForm, EduInfoForm


def manage_home(request):

    return render(request, 'manage/manage_home.html', {

    })


@login_required
def manage_baseinfo(request):
    user = request.user
    try:
        baseinfo = BaseInfo.objects.filter(user=user)[0]
    except Exception,e:
        baseinfo = None
        print e

    if request.method == "POST":
        form = BaseInfoForm(request.POST, instance=baseinfo)
        if form.is_valid():
            baseinfo = form.save(commit=False)
            baseinfo.user = user
            baseinfo.save()
    else:
        form = BaseInfoForm(instance=baseinfo)

    return render(request, 'manage/private/baseinfo.html', {
        'form': form,
    })


@login_required
def manage_eduinfo(request):
    user = request.user
    try:
        eduinfo = EduInfo.objects.filter(user=user)[0]
    except Exception,e:
        eduinfo = None
        print e

    if request.method == "POST":
        form = EduInfoForm(request.POST, instance=eduinfo)
        if form.is_valid():
            form.save()
    else:
        form = EduInfoForm(instance=eduinfo)

    return render(request, 'manage/private/eduinfo.html', {
        'form': form,
    })
