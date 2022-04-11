import pytest

# from django.contrib.auth import get_user_model
# from accounts.models import CustomUser
from django.core.management import call_command
from inventory.models import (
    Category,
    Product,
    Media,
    ProductInventory,
    ProductAttribute,
    ProductType,
    Brand,
    ProductAttributeValue,
)
from order.models import Order, OrderItem


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser("admin", "a@a.com", "password")


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures
    """
    with django_db_blocker.unblock():

        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        # call_command("loaddata", "db_type_fixture.json")
        # call_command("loaddata", "db_brand_fixture.json")
        # call_command("loaddata", "db_product_inventory_fixture.json")
        # call_command("loaddata", "db_product_attribute_fixture.json")
        # call_command("loaddata", "db_product_attribute_value_fixture.json")
        # call_command("loaddata", "db_product_attribute_values_fixture.json")
        # call_command("loaddata", "db_media_fixture.json")
        # call_command("loaddata", "db_stock_fixture.json")
        # call_command("loaddata", "db_product_type_attribute_fixture.json")


@pytest.fixture
def single_category(db):
    return Category.objects.create(name="defaul", slug="default")


@pytest.fixture
def category_with_child(db):
    parent = Category.objects.create(name="parent", slug="parent")
    parent.childern.create(name="child", slug="child")
    child = parent.childern.first()
    return child


@pytest.fixture
def single_product(db, category_with_child):
    product = Product.objects.create(
        web_id="123456789",
        slug="default",
        name="default",
        category=category_with_child,
        is_active=True,
    )
    return product


@pytest.fixture
def category_with_multiple_children(db):
    record = Category.objects.build_tree_nodes(
        {
            "id": 1,
            "name": "parent",
            "slug": "parent",
            "children": [
                {
                    "id": 2,
                    "parent_id": 1,
                    "name": "child",
                    "slug": "child",
                    "children": [
                        {
                            "id": 3,
                            "parent_id": 2,
                            "name": "grandchild",
                            "slug": "grandchild",
                        }
                    ],
                }
            ],
        }
    )
    category = Category.objects.bulk_create(record)
    return category


@pytest.fixture
def product_type(db, product_attribute):
    product_type = ProductType.objects.create(name="default")
    product_attribute = product_attribute

    product_type.product_type_attributes.add(product_attribute)

    return product_type


@pytest.fixture
def product_attribute(db):
    product_attribute = ProductAttribute.objects.create(
        name="default", description="default"
    )
    return product_attribute


@pytest.fixture
def brand(db):
    brand = Brand.objects.create(name="default")
    return brand


@pytest.fixture
def single_sub_product_with_media_and_attributes(
    db, single_product, product_type, brand, product_attribute_value
):

    sub_product = ProductInventory.objects.create(
        sku="123456789",
        upc="100000000001",
        product_type=product_type,
        product=single_product,
        brand=brand,
        is_active=True,
        is_default=True,
        retail_price="199.99",
        store_price="99.99",
        is_digital=False,
        weight=1000.0,
    )

    media = Media.objects.create(
        product_inventory=sub_product,
        img_url="images/default.png",
        alt_text="default",
        is_feature=True,
    )

    product_attribute_value = product_attribute_value
    sub_product.attribute_values.add(product_attribute_value)

    return {
        "inventory": sub_product,
        "media": media,
        "attribute": product_attribute_value,
    }


@pytest.fixture
def product_attribute_value(db, product_attribute):
    product_attribute_value = ProductAttributeValue.objects.create(
        product_attribute=product_attribute,
        attribute_value="default",
    )
    return product_attribute_value


@pytest.fixture
def order_item(
    db, single_product, product_type, brand, product_attribute_value, create_admin_user
):
    user = create_admin_user
    sub_product = ProductInventory.objects.create(
        sku="123456789",
        upc="100000000001",
        product_type=product_type,
        product=single_product,
        brand=brand,
        is_active=True,
        is_default=True,
        retail_price="199.99",
        store_price="99.99",
        is_digital=False,
        weight=1000.0,
    )

    media = Media.objects.create(
        product_inventory=sub_product,
        img_url="images/default.png",
        alt_text="default",
        is_feature=True,
    )

    product_attribute_value = product_attribute_value
    sub_product.attribute_values.add(product_attribute_value)

    order_item = OrderItem.objects.create(
        user=user,
        ordered=False,
        item=sub_product,
        quantity=1,
        price="500.00",
    )
    order_item.price = order_item.get_final_price()

    order = Order.objects.create(
        user=user,
        start_date="2022-04-10T06:41:41",
        ordered_date="2022-04-10T06:41:41",
        ordered=False,
        name="murtatha",
        phone_number="07806017024",
        address="ira",
        address_2="asd",
        price="500.00",
    )
    order.items.set([order_item])
    order.price = order.get_total()

    return {
        "order": order,
        "order_item": order_item,
        "media": media,
        "attribute": product_attribute_value,
    }


@pytest.fixture
def ordered_order(
    db, single_product, product_type, brand, product_attribute_value, create_admin_user
):
    user = create_admin_user
    sub_product = ProductInventory.objects.create(
        sku="123456789",
        upc="100000000001",
        product_type=product_type,
        product=single_product,
        brand=brand,
        is_active=True,
        is_default=True,
        retail_price="199.99",
        store_price="99.99",
        is_digital=False,
        weight=1000.0,
    )

    media = Media.objects.create(
        product_inventory=sub_product,
        img_url="images/default.png",
        alt_text="default",
        is_feature=True,
    )

    product_attribute_value = product_attribute_value
    sub_product.attribute_values.add(product_attribute_value)

    order_item = OrderItem.objects.create(
        user=user,
        ordered=True,
        item=sub_product,
        quantity=1,
        price="99.99",
    )
    order = Order.objects.create(
        user=user,
        start_date="2022-04-10T06:41:41",
        ordered_date="2022-04-10T06:41:41",
        ordered=True,
        name="murtatha",
        phone_number="07806017024",
        address="ira",
        address_2="asd",
        price="500.00",
    )
    order.items.set([order_item])
    return {
        "order": order,
        "order_item": order_item,
        "media": media,
        "attribute": product_attribute_value,
    }
