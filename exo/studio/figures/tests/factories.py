import factory

from factory.django import DjangoModelFactory

from users.tests import factories as user_factories
from studio.figures.models import Model3D


class Model3DFactory(DjangoModelFactory):
    class Meta:
        model = Model3D

    designer = factory.SubFactory(user_factories.UserFactory)
    name = factory.Sequence(lambda n: "model %03d" % n)
