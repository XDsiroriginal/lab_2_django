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

    def __str__(self):
        return self.username + ' профиль'

class Category(models.Model):
    category_full_name = models.CharField(max_length=100)
    category_char = models.CharField(max_length=1, blank=False)

    def __str__(self):
        return self.category_full_name

class application(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ALL_STATUS = (
        ('n', 'Новая заявка'),
        ('w', 'Принята в работу'),
        ('c', 'Выполнена'),
        ('r', 'Отклонена')
    )
    status = models.CharField(max_length=1, choices=ALL_STATUS, blank=False, default='n')
    date = models.DateField(auto_now=False, auto_now_add=True)

    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images/', blank=False, null=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    comment = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.id)])

    def __str__(self):
        return self.title