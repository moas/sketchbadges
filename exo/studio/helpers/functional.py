import datetime

from django.utils import timezone


def compute_age(born):
    assert isinstance(born, datetime.date)

    today = timezone.datetime.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age
