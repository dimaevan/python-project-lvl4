from django import forms
from . models import Task
from django.contrib.auth.models import User


class UserModelChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class TaskForm(forms.ModelForm):
    executor = UserModelChoiceField(User.objects.all())

    class Meta:
        model = Task
        exclude = ('author',)

