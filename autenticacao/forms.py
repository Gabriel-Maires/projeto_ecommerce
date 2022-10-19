from .models import Usuario
from django.contrib.auth import forms as auth_form


class UserChangeForm(auth_form.UserChangeForm):
    class Meta(auth_form.UserChangeForm.Meta):
        model = Usuario


class UserCreationForm(auth_form.UserCreationForm):
    class Meta(auth_form.UserCreationForm.Meta):
        model = Usuario

