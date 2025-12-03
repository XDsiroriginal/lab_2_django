from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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

class Profile(models.Model):
    avatarlink = models.TextField()
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        permissions = (
            ('worker', 'Работник'),
            ('user', 'Пользователь')
        )

class application(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ALL_STATUS = (
        ('n', 'Новая заявка'),
        ('w', 'Принята в работу'),
        ('c', 'Выполнена'),
        ('r', 'Отклонена')
    )
    status = models.CharField(max_length=1, choices=ALL_STATUS, blank=True, default='n')

    ALL_CATEGORIES = (
        ('3', '3D Дизайн'),
        ('2', '2D Дизайн'),
        ('e', 'Эскиз'),
        ('l', 'Логотип')
    )
    categories = models.CharField(max_length=1, choices=ALL_CATEGORIES, blank=True, default='n')

    image = models.ImageField(upload_to='images/')
    username = models.OneToOneField(User, on_delete=models.CASCADE)