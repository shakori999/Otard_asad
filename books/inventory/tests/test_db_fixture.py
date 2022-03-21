from django.db import IntegrityError
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
def test_inventory_category_dbfixture(db, db_fixture_setup, id, name, slug, is_active):
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
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, create_at, updated_at",
    [
        (
            1,
            "45425810",
            "widstar running sneakers",
            "widestart-running-sneakers",
            "loarem impsum",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            "45434425",
            "impcat puse dance shoes ",
            "impcat-puse-dance-shoes",
            "loarem impsum",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_product_dbfixture(
    db,
    db_fixture_setup,
    id,
    web_id,
    name,
    slug,
    description,
    is_active,
    create_at,
    updated_at,
):
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert result.web_id == web_id
    assert result.name == name
    assert result.web_id == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == create_at
    assert result_updated_at == updated_at


def test_inventory_db_product_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id=123456789)
    with pytest.ra(IntegrityError):
        product_factory.create(web_id=123456789)


def test_inventory_db_product_insert_data(db, product_factory, category_factory):
    new_category = category_factory.create()
    new_product = product_factory.create(category=(1, 36))

    result_product_category = new_product.category.all().count()
    assert "web_id_" in new_product.web_id
    assert result_product_category == 2
