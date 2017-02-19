from django.conf import settings
from django.test.utils import override_settings
from test_plus import TestCase
from badges.models import Badge

from users.tests.factories import GroupFactory, UserFactory
from .factories import Model3DFactory


@override_settings(MINIMUM_UPLOAD_FOR_COLLECTOR_BADGE=2)
class TestCollectorBadge(TestCase):

    BADGE_LEVEL = settings.BADGE_LEVEL.BADGE_COLLECTOR.value

    def setUp(self):
        group = GroupFactory.create(name=settings.DESIGNER_GROUP_NAME)
        self.designer = UserFactory.create(groups=[group, ])

    def test_model_counter_lower_then_minimum(self):
        Model3DFactory.create(designer=self.designer)
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 0)

    def test_model_counter_equal_minimum(self):
        for _ in range(2):
            Model3DFactory.create(designer=self.designer)
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 1)

    def test_model_counter_gran_than_minimum(self):
        for _ in range(3):
            Model3DFactory.create(designer=self.designer)
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 1)

    def test_model_counter_gran_than_minimum_and_more(self):
        for _ in range(3):
            Model3DFactory.create(designer=self.designer)
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 1)

        Model3DFactory.create(designer=self.designer)
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 1)
