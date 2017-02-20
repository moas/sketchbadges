from django.conf import settings
from braces.views import GroupRequiredMixin
from badges.utils import MetaBadgeMeta


class BadgeMixin(metaclass=MetaBadgeMeta):
    one_time_only = True

    def award_ceremony(self, instance):
        instance.refresh_from_db()
        super().award_ceremony(instance)


class DesignerGroupMixin(GroupRequiredMixin):
    group_required = settings.DESIGNER_GROUP_NAME

    def check_membership(self, groups):
        """ Check required group(s) """
        user_groups = self.request.user.groups.values_list("name", flat=True)
        return set(groups).intersection(set(user_groups))
