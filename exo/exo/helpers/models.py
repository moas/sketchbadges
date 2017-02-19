from django.db import models

from model_utils.models import AutoCreatedField, AutoLastModifiedField


class CommonModels(models.Model):
    created = AutoCreatedField()
    updated = AutoLastModifiedField()
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
