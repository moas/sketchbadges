from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersConfig(AppConfig):
    name = 'studio.users'
    verbose_name = _('List of users')

    def ready(self):
        from .meta_badges import register_badges
        register_badges()
