from django import forms
from . models import Task


class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))


    class Meta:
        model = Task
        exclude = ('author',)
