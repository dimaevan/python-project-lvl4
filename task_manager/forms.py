from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from django import forms


class UserUpdateForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='User',
                               help_text='Required field. No more than 150 characters. Only letters, numbers and '
                                         '@/./+/-/_ characters.')
    first_name = forms.CharField(max_length=100, label='First name')
    last_name = forms.CharField(max_length=100, label='Last name')
    password1 = forms.CharField(max_length=100, label='Password')
    password2 = forms.CharField(max_length=100, label='Password confirm', help_text='Please enter your password again '
                                                                                    'to confirm.')


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']
