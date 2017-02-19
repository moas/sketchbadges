from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from badges.utils import MetaBadge

from studio.helpers.mixins import BadgeMixin
from ..figures.models import Model3D


class ModelBadgeMixin:
    model = Model3D

    def get_user(self, instance):
        return instance.designer


class StarBadge(BadgeMixin, ModelBadgeMixin, MetaBadge):
    id = 'star'
    title = _('Star')
    description = _('Award for %(val)s views and more') % {'val': settings.MINIMUM_VIEWS_FOR_STAR_BADGE}
    level = '1'

    def check_view_counter(self, instance):
        return instance.view_counter >= settings.MINIMUM_VIEWS_FOR_STAR_BADGE


class CollectorBadge(BadgeMixin, ModelBadgeMixin, MetaBadge):
    id = 'collector'
    title = _('Collector')
    description = _('Award for %(val)s models or more') % {'val': settings.MINIMUM_UPLOAD_FOR_COLLECTOR_BADGE}
    level = '2'

    def check_model_counter(self, instance):
        return self.model.objects.filter(
            designer=instance.designer
        ).count() >= settings.MINIMUM_UPLOAD_FOR_COLLECTOR_BADGE


def register_badges():
    for klass in (CollectorBadge, StarBadge):
        klass()
