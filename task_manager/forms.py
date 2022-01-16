from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django import forms


class UserUpdateForm(UserCreationForm):
    # Texts:

    text_help_username = _('Required field. No more than 150 characters. Only letters, numbers and '
                           '@/./+/-/_ characters.')
    text_first_name = _('First name')
    text_last_name = _('Last name')
    text_password = _('Password')

    username = forms.CharField(max_length=100, label=_('User'),
                               help_text=text_help_username)
    first_name = forms.CharField(max_length=100, label=text_first_name, required=False)
    last_name = forms.CharField(max_length=100, label=text_last_name, required=False)
    password1 = forms.CharField(max_length=100, label=text_password)
    password2 = forms.CharField(max_length=100,
                                label=_('Password confirm'), help_text=_('Please enter your password again '
                                                                         'to confirm.'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']
