# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    gender = models.CharField(
        _('Gender'),
        max_length=4,
        choices=Choices(*settings.USER_GENDERS),
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse_lazy('users:detail', kwargs={'username': self.username})

    def get_full_name(self):
        ret = super().get_full_name()
        return '{} {}'.format(self.gender, ret or self.name)

    def get_short_name(self):
        ret = super().get_short_name()
        return ret or self.name
