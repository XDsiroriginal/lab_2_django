from tkinter import Image
from urllib import request

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic
from .models import ImageContent

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


