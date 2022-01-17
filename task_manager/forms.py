from task_manager.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class UserUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, label=_('First name'))
    last_name = forms.CharField(required=True, label=_('Last name'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']
