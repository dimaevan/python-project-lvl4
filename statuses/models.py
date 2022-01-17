from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    created = models.DateTimeField(verbose_name=_('Data creation'), auto_now_add=True)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.name
