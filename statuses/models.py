from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.status
