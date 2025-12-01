from django.db import models
from django.urls import reverse

class ImageContent(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField()

    def __str__(self):
        return self.title

    def get_image_title(self):
        return self.title

    def get_image_link(self):
        return self.link

    def get_absolute_url(self):
        return reverse('image-detail', args=[str(self.id)])