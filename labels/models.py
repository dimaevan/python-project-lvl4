from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Label'))

    def __str__(self):
        return self.name
