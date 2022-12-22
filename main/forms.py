from django import forms
from .models import UsersFiles, UsersImage
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import PasswordInput, ModelForm
from django.core.validators import validate_email
import os
from django.conf import settings


# форма авторизации
class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, label='Password')

# форма регистрации
class RegisterForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
    username = forms.CharField(min_length=3, max_length=10, required=True, label='Name', validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Может содержать только латинские буквы и цифры',
            code='invalid_username'
        ),
    ])
    email = forms.CharField(min_length=3, required=True, label='Email')
    password = forms.CharField(widget=PasswordInput(), required=True, label='Password')
    password_confirm = forms.CharField(widget=PasswordInput(), required=True, label='Повторите пароль')

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        # валидация паролей
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError(
                {'password_confirm': "Пароли не совпадают", 'password': ''}
            )
            # валидация никнейма
        username = self.cleaned_data.get("username")

        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError({'username': "Такой логин уже занят"})

        # валидация email
        try:
            validate_email(self.cleaned_data.get("email"))
        except ValidationError as e:
                raise forms.ValidationError({'email': "Email не является валидным адресом"})
        return cleaned_data


class FilesForm(forms.ModelForm):
    class Meta:
        model = UsersFiles
        fields={'title', 'file', 'userName'}
    title=forms.CharField(max_length=100, label="File name", required=True)
    file = forms.FileField()
    userName = forms.CharField(max_length=150)

class ImageForm(forms.ModelForm):
    class Meta:
        model = UsersImage
        fields={'title', 'image', 'username'}

    title = forms.CharField(max_length=20)
    image = forms.ImageField()
    username = forms.CharField(max_length=150)
