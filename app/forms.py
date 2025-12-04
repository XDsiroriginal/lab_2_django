from random import choices

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import validate_cyrillic_and_spaces, validate_image
from .models import application

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