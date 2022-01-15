from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Label'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Data creation'))

    def __str__(self):
        return self.name
