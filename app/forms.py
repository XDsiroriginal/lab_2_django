from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .validators import validate_cyrillic_and_spaces, validate_image, validate_login
from .models import application, Category


class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True, label='Логин пользователя', validators=[validate_login])
    email = forms.EmailField(required=True, label='Электронная почта')
    first_name = forms.CharField(required=True, label='Имя', validators=[validate_cyrillic_and_spaces])
    last_name = forms.CharField(required=True, label='Фамилия', validators=[validate_cyrillic_and_spaces])
    patronymic = forms.CharField(required=True, label='Отчество', validators=[validate_cyrillic_and_spaces])
    consent_to_the_processing_of_personal_data = forms.BooleanField(required=True,
                                                                    label='Согласие на обработку персональных данных')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'patronymic', 'email', 'password1', 'password2']


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
        fields = ('status', 'comment', 'image')
        labels = {
            'status': 'Изменить статус заявки',
            'comment': 'Коментарий',
            'image': 'новое изображение'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.status != 'n':
            self.fields['status'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        comment = cleaned_data.get('comment')

        if status == 'w' and not comment:
            self.add_error('comment', 'При выборе статуса "в работе" комментарий обязателен.')

        if status == 'c':
            if not self.files.get('image'):
                self.add_error('image', 'При выборе статуса "завершено" необходимо прикрепить изображение.')
        return cleaned_data


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
