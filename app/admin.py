from django.contrib import admin
from .models import ImageContent, Profile, application, Category

admin.site.register(ImageContent)
admin.site.register(Profile)
admin.site.register(application)
admin.site.register(Category)