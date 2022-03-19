import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from inventory.models import *


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "cat_name_%d" % n)
    slug = fake.lexify(text="cat_slug_??????")


register(CategoryFactory)
