from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils.translation import ugettext_lazy as _
from badges.utils import MetaBadge

from studio.helpers.mixins import BadgeMixin
from studio.helpers.functional import compute_age


class PionneerBadge(BadgeMixin, MetaBadge):
    model = get_user_model()

    id = 'pionneer'
    title = _('Pionneer')
    description = _('Award for registered user since %(val)s year(s)') % {
        'val': settings.MINIMUM_YEAR_FOR_PIONNEER_BADGE}
    level = '3'

    def __init__(self):
        super(self.__class__, self).__init__()
        user_logged_in.connect(self._auth_callback, sender=self.model)
        user_logged_out.connect(self._auth_callback, sender=self.model)

    def _auth_callback(self, **kwargs):
        self.award_ceremony(instance=kwargs['user'])

    def get_user(self, instance):
        return instance

    def check_anniversary(self, instance):
        if instance.groups.filter(name=settings.DESIGNER_GROUP_NAME).exists() is False:
            return False
        date_joined = instance.date_joined.date()
        age = compute_age(date_joined)
        return age >= settings.MINIMUM_YEAR_FOR_PIONNEER_BADGE


def register_badges():
    for klass in (PionneerBadge, ):
        klass()
