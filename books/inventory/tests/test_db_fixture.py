import pytest
from inventory.models import *


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        ("ac1f0314-cb65-4c91-a73e-97791799c83f", "fashoin", "fashoin", 1),
        ("869a7792-5f80-41ec-8b1d-addbbce1c6f2", "trainers", "trainers", 1),
        ("68fb201a-4f37-4ec5-8285-b511c2df118e", "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbgixture(db, db_fixture_setup, id, name, slug, is_active):
    result = Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashoin", 1),
        ("trainers", 1),
        ("baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(db, category_factory, slug, is_active):
    result = category_factory.create(slug=slug, is_active=is_active)
    print(result.name)
    # assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active
