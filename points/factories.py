import factory
from points.models import Points

class PointsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Points

    name = factory.Sequence(lambda n: f"Name of points number {n}")
    location = factory.Sequence(lambda n: f"Location - {n}")
    description = factory.Sequence(lambda n: f"Description - {n}")