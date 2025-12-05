from random import choices
from unicodedata import category

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.defaulttags import comment

from .validators import validate_cyrillic_and_spaces, validate_image
from .models import application, Category

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Электронная почта')
    first_name = forms.CharField(required=True, label='Имя', validators=[validate_cyrillic_and_spaces])
    last_name = forms.CharField(required=True, label='Фамилия', validators=[validate_cyrillic_and_spaces])
    patronymic = forms.CharField(required=True, label='Отчество', validators=[validate_cyrillic_and_spaces])
    consent_to_the_processing_of_personal_data = forms.BooleanField(required=True, label='Согласие на обработку персональных данных')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'patronymic','email', 'password1', 'password2']

class LoginChangeForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')

class FirstNameChangeForm(forms.Form):
    first_name = forms.CharField(required=True, label='Имя', validators=[validate_cyrillic_and_spaces])

class LastNameChangeForm(forms.Form):
    last_name = forms.CharField(required=True, label='Фамилия', validators=[validate_cyrillic_and_spaces])

class EmailChangeForm(forms.Form):
    email = forms.EmailField(required=True, label='Электронная почта')

class PatronymicChangeForm(forms.Form):
    patronymic = forms.CharField(required=True, label='Отчество', validators=[validate_cyrillic_and_spaces])

# class ApplicationForm(forms.Form):
#     title = forms.CharField(required=True, label='Название заявки')
#     description = forms.CharField(required=True, label='Введите описание заявки')
#     categories = forms.ChoiceField(
#         required=True,
#         label='Категория заявки',
#         choices=[
#             ('3', '3D Дизайн'),
#             ('2', '2D Дизайн'),
#             ('e', 'Эскиз'),
#             ('l', 'Логотип'),
#         ]
#     )
#     image = forms.ImageField(required=True, validators=[validate_image])

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = application
        fields = ['title', 'description', 'categories', 'image']
        labels = {
            'title': 'Название заявки',
            'description': 'Введите описание заявки',
            'categories': 'Категория заявки',
        }
        widgets = {
            'description': forms.Textarea(),
        }

class ApplicationChangeForm(forms.ModelForm):
    class Meta:
        model = application
        fields = ('status', 'categories', 'comment', 'image')
        labels = {
            'status': 'Изменить статус заявки',
            'categories': 'Изменит категорию',
            'comment': 'Коментарий',
            'image': 'новое изображение'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.status != 'n':
            self.fields['status'].disabled = True
        if self.instance and self.instance.status == 'n':
            self.fields['image'].required=True
        if self.instance and self.instance.status == 'n':
            self.fields['comment'].required=True

class CreateNewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_full_name', 'category_char')
        labels = {
            'category_full_name': 'Полное название категории',
            'category_char': 'короткое название категории',
        }

class CategoryChangeForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_full_name', 'category_char')
        labels = {
            'category_full_name': 'Полное название категории',
            'category_char': 'короткое название категории',
        }