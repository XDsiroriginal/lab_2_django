#from tkinter import Image
from idlelib.pyparse import trans
from urllib import request

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic
from .models import ImageContent, Profile

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