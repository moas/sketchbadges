from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FiguresConfig(AppConfig):
    name = 'studio.figures'
    verbose_name = _('List of model')

    def ready(self):
        from .meta_badges import register_badges
        register_badges()
