from django.db import models
from task_manager.models import User
from statuses.models import Status
from labels.models import Label
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name of task'))
    description = models.TextField(null=True, verbose_name=_('Descriptions'))
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Executor',
                                 verbose_name=_('Executor'))

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Author',
                               verbose_name=_('Author'))
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name=_('Status'))
    labels = models.ManyToManyField(Label, blank=True, verbose_name=_('Label'))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _("Task")

    def __str__(self):
        return self.name
