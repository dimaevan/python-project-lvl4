from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserUpdateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']
