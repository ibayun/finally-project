from django import forms
from django.contrib.auth.hashers import make_password

from users.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",

        )
        widgets = {
            "password": forms.PasswordInput
        }
        widgets = {
            "username": forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'I_bayun',
                'title': 'Сюда необходимо ввести ваш логин.'
            }),
            "email": forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'email@email.email',
                'title': 'Введите ваш email.'
            }),
            "password": forms.PasswordInput(attrs={
                'class': 'form-group',
                'placeholder': 'qwerty',
                'title': 'Введите ваш пароль.'
            }),
            "first_name": forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Семен',
                'title': 'Сюда необходимо ввести ваше имя.'
            }),
            "last_name": forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Петров',
                'title': 'Сюда необходимо ввести вашу фамилию.'
            }),
        }

    def save(self, commit=True):
        password = (
            make_password(
                self.cleaned_data['password']
            )
        )
        self.instance.password = password
        self.cleaned_data['password'] = password
        return super().save(commit)
