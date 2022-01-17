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
            return queryset.filter(author=self.request.user).order_by('pk')
        return queryset

    labels = django_filters.filters.ModelChoiceFilter(queryset=Label.objects.all(),
                                                      label=_('LabelOne'))

    class Meta:
        model = Task
        fields = ['name', 'status', 'executor', 'labels', 'self_task']
        filter_overrides = {
            django_filters.filters.BooleanFilter: {
                'filter_class': django_filters.filters.BooleanFilter,
                'extra': lambda f: {'widget': forms.widgets.CheckboxInput},
            },
        }
