import factory

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from factory.django import DjangoModelFactory


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    name = factory.Sequence(lambda n: "user %03d" % n)

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)

