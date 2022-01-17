import django_filters
from .models import Task
from django import forms
from django.utils.translation import gettext as _
from labels.models import Label


class TaskFilter(django_filters.FilterSet):
    text = _('Only your tasks')
    self_task = django_filters.BooleanFilter(widget=forms.widgets.CheckboxInput,
                                             field_name='author',
                                             label=text,
                                             method='filter_by_author')

    def filter_by_author(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        else:
            return queryset

    label = django_filters.filters.ModelChoiceFilter(
            queryset=Label.objects.all(),
            label=_('Label')
        )

    class Meta:
        model = Task
        fields = ['name', 'status', 'executor', 'label', 'self_task']
