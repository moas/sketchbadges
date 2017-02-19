from badges.utils import MetaBadgeMeta


class BadgeMixin(metaclass=MetaBadgeMeta):
    one_time_only = True

    def award_ceremony(self, instance):
        instance.refresh_from_db()
        super().award_ceremony(instance)
