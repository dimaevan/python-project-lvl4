from django.db import models
from django.utils.translation import gettext as _


class Status(models.Model):
    status = models.CharField(max_length=100, verbose_name=_('Name'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Data creation'))

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.status
