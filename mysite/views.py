import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import LoginForm, RegForm
from users.models import UserProfile


def home(request):

    context = {}
    return render(request, 'home.html', context)

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)

def logout(request):
    context = {}
    auth.logout(request)
    return render(request, 'home.html', context)
def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            user_name = reg_form.cleaned_data['user_name']
            stu_id = reg_form.cleaned_data['stu_id']
            major = reg_form.cleaned_data['major']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            user_profile = UserProfile(user=user, user_name=user_name, stu_id=stu_id, major=major)
            user_profile.save()
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)


def myinfo(request):
    context = {}
    try:
        context['userprofile'] = (UserProfile.objects.filter(user=request.user))[0]
    except:
        pass
    return render(request, 'myinfo.html', context)