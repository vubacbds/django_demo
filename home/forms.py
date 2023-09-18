from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Tạo ra form từ các trường của Models
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
