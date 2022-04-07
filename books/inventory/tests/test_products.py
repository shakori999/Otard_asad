from inventory.models import Product


def test_insert_single_product_with_sub_category(single_product):
    new_product = single_product
    get_product = Product.objects.all().last()
    assert new_product.id == get_product.id
