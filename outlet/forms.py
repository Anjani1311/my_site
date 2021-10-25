
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text ',
                'type': "text",
                'placeholder': "Enter User Name..."
            }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'text fname',
                'type': "fname",
                'placeholder': "Enter Password..."
            }))


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text fname',
                'type': "fname",
                'placeholder': "First Name..."
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text lname',
                'type': "lname",
                'placeholder': "Last Name..."
            }
        )

    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text ',
                'type': "text",
                'placeholder': "User Name..."
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'text fname',
                'type': "fname",
                'placeholder': "Email..."
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'text fname',
                'type': "fname",
                'placeholder': "Password..."
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'text fname',
                'type': "fname",
                'placeholder': "Confirm Password..."
            }
        )
    )
    dept = forms.CharField(
        widget=forms.Select(
            choices=DeptChoice,
            attrs={
                'class': 'text ',
                'type': "text",
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1',
                  'password2', 'dept', 'status', 'is_teacher', 'is_student')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            'Heading',
            'category',
            'subcategory',
            'description',
            'publish_date',
            'image',
        )

    category = forms.CharField(
        widget=forms.Select(
            choices=NewsDeptChoice,
        )
    )
    publish_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': "date",
            }
        )
    )
