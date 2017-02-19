from django.conf import settings
from django.db.models import F
from django.test.utils import override_settings
from test_plus import TestCase
from badges.models import Badge

from users.tests.factories import GroupFactory, UserFactory
from .factories import Model3DFactory


@override_settings(MINIMUM_VIEWS_FOR_STAR_BADGE=5)
class TestStarBadge(TestCase):

    BADGE_LEVEL = "1"

    def setUp(self):
        group = GroupFactory.create(name=settings.DESIGNER_GROUP_NAME)
        self.designer = UserFactory.create(groups=[group, ])

    def test_new_model(self):
        Model3DFactory.create(designer=self.designer)
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 0)

    def test_model_with_view_lower_then_minimum(self):
        Model3DFactory.create(
            designer=self.designer,
            view_counter=(settings.MINIMUM_VIEWS_FOR_STAR_BADGE - 1)
        )
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 0)

    def test_model_with_view_equal_minimul(self):
        Model3DFactory.create(
            designer=self.designer,
            view_counter=settings.MINIMUM_VIEWS_FOR_STAR_BADGE
        )
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 1)

    def test_model_with_view_gran_than_minimum(self):
        Model3DFactory.create(
            designer=self.designer,
            view_counter=(settings.MINIMUM_VIEWS_FOR_STAR_BADGE + 1)
        )
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 1)

    def test_model_with_gran_than_minimum_and_more(self):
        model = Model3DFactory.create(
            designer=self.designer,
            view_counter=(settings.MINIMUM_VIEWS_FOR_STAR_BADGE + 1)
        )
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 1)

        model.view_counter = F('view_counter') + 5
        model.save()
        counter = Badge.objects.filter(user=self.designer, level=self.BADGE_LEVEL).count()
        self.assertEqual(counter, 1)
