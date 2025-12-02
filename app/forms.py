from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginChangeForm(forms.Form):
    username = forms.CharField(required=True)

class FirstNameChangeForm(forms.Form):
    first_name = forms.CharField(required=True)

class LastNameChangeForm(forms.Form):
        last_name = forms.CharField(required=True)

class EmailChangeForm(forms.Form):
    email = forms.EmailField(required=True)