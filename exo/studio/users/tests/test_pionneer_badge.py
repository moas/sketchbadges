import unittest.mock as mock

from django.conf import settings
from django.test.utils import override_settings
from test_plus import TestCase
from badges.models import Badge

from .factories import UserFactory, GroupFactory


@override_settings(MINIMUM_YEAR_FOR_PIONNEER_BADGE=1)
class TestPionneerBadge(TestCase):

    BADGE_LEVEL = settings.BADGE_LEVEL.BADGE_PIONNEER.value

    def setUp(self):
        self.group = GroupFactory.create(name=settings.DESIGNER_GROUP_NAME)

    def test_designer_recent_joined_badge(self):
        designer = UserFactory.create(groups=[self.group, ])
        counter = Badge.objects.filter(user=designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 0)

    def test_designer_date_joined_since_one_year(self):
        with mock.patch("studio.users.meta_badges.compute_age", return_value=1):
            designer = UserFactory.create(groups=[self.group, ])
            counter = Badge.objects.filter(user=designer, level=self.BADGE_LEVEL).count()
            self.assertEqual(counter, 1)

    def test_designer_date_joined_since_more_one_year(self):
        with mock.patch("studio.users.meta_badges.compute_age", return_value=5):
            designer = UserFactory.create(groups=[self.group, ])
            counter = Badge.objects.filter(user=designer, level=self.BADGE_LEVEL).count()
            self.assertEqual(counter, 1)

    def test_designer_date_joined_since_one_year_immutable(self):
        with mock.patch("studio.users.meta_badges.compute_age", return_value=1):
            designer = UserFactory.create(groups=[self.group, ])
            counter = Badge.objects.filter(user=designer, level=self.BADGE_LEVEL).count()
            self.assertEqual(counter, 1)

        with mock.patch("studio.users.meta_badges.compute_age", return_value=1):
            designer.last_name = 'test_name'
            designer.save()
            counter = Badge.objects.filter(user=designer, level=self.BADGE_LEVEL).count()
            self.assertEqual(counter, 1)

        with mock.patch("studio.users.meta_badges.compute_age", return_value=4):
            designer.first_name = 'test_name'
            designer.save()
            counter = Badge.objects.filter(user=designer, level=self.BADGE_LEVEL).count()
            self.assertEqual(counter, 1)
