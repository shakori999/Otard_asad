import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from inventory.models import *

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = fake.lexify(text="cat_name_??????")
    slug = fake.lexify(text="cat_slug_??????")

register(CategoryFactory)