# from tkinter import Image
from idlelib.pyparse import trans
from urllib import request
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import generic
from .models import ImageContent, Profile
from .forms import RegisterForm, LoginChangeForm, FirstNameChangeForm, LastNameChangeForm, EmailChangeForm


def index(request):
    return render(
        request,
        'app/index.html',
    )

def to_logout(request):
    return render(
        request,
        'registration/to_logout.html'
    )


class ImageDetailView(generic.DetailView):
    model = ImageContent


class ImageListView(generic.ListView):
    model = ImageContent
    context_object_name = 'image_list'
    paginate_by = 9


def to_profile(request):
    user = request.user
    if user.is_authenticated:
        profile = user.profile
        return render(
            request,
            'app/profile.html',
            {'profile': profile}
        )
    else:
        return render(
            request,
            'app/profile.html',
        )


def change_user_avatar(request, pk):
    image = ImageContent.objects.get(pk=pk)
    user = request.user
    profile = user.profile
    profile.avatarlink = image.link
    profile.save()
    return render(
        request,
        'app/profile.html',
        {'profile': profile}
    )


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(avatarlink='none.jpg', username=user)
            profile.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def login_change(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user

    if request.method == 'POST':
        form = LoginChangeForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['username']
            if User.objects.filter(username=new_username).exists() and new_username != user.username:
                return render(request, 'registration/login_change.html',
                              {'form': form, 'error_message': 'Это имя пользователя уже занято.'})
            user.username = new_username
            user.save()
            profile = user.profile
            profile.save()
            return redirect('profile')
    else:
        form = LoginChangeForm(initial={'username': user.username})

    return render(request, 'registration/login_change.html', {'form': form})

def first_name_change(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user

    if request.method == 'POST':
        form = FirstNameChangeForm(request.POST)
        if form.is_valid():
            new_user_firstname = form.cleaned_data['first_name']
            user.first_name = new_user_firstname
            user.save()
            return redirect('profile')
    else:
        form = FirstNameChangeForm(initial={'first_name': user.first_name})

    return render(request, 'registration/first_name_change.html', {'form': form})

def last_name_change(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user

    if request.method == 'POST':
        form = LastNameChangeForm(request.POST)
        if form.is_valid():
            new_user_lastname = form.cleaned_data['last_name']
            user.last_name = new_user_lastname
            user.save()
            return redirect('profile')
    else:
        form = LastNameChangeForm(initial={'last_name': user.last_name})

    return render(request, 'registration/last_name_change.html', {'form': form})

def email_change(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user

    if request.method == 'POST':
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            new_user_email = form.cleaned_data['email']
            user.email = new_user_email
            user.save()
            return redirect('profile')
    else:
        form = EmailChangeForm(initial={'email': user.email})

    return render(request, 'registration/email_change.html', {'form': form})
