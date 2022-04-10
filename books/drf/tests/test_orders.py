import json
from datetime import datetime

from .utils import convert_to_dot_notation


def test_get_ordered_orders_summary(api_client, order_item):
    fixture = convert_to_dot_notation(order_item)

    start_date = fixture.order.start_date
    str2 = str(start_date)
    start_date_2 = str2.replace(" ", "T")
    endpoint = f"/api/order/order-summary/"
    response = api_client().get(endpoint)
    expected_json = [
        {
            "items": [
                {
                    "ordered": fixture.order_item.ordered,
                    "item": {
                        "id": fixture.order_item.item.id,
                        "sku": fixture.order_item.item.sku,
                        "store_price": fixture.order_item.item.store_price,
                        "is_default": fixture.order_item.item.is_default,
                        "brand": {"name": fixture.order_item.item.brand.name},
                        "product": {
                            "name": fixture.order_item.item.product.name,
                            "web_id": fixture.order_item.item.product.web_id,
                        },
                        "weight": fixture.order_item.item.weight,
                        "media": [
                            {
                                "img_url": fixture.media.img_url.url,
                                "alt_text": fixture.media.alt_text,
                            }
                        ],
                        "attributes": [
                            {
                                "attribute_value": fixture.attribute.attribute_value,
                                "product_attribute": {
                                    "id": fixture.attribute.id,
                                    "name": fixture.attribute.product_attribute.name,
                                    "description": fixture.attribute.product_attribute.description,
                                },
                            }
                        ],
                        "product_type": fixture.order_item.item.product_type.id,
                        "promotion_price": None,
                    },
                    "quantity": fixture.order_item.quantity,
                }
            ],
            "start_date": start_date_2,
            "ordered_date": fixture.order.ordered_date,
            "ordered": fixture.order.ordered,
            "name": fixture.order.name,
            "phone_number": fixture.order.phone_number,
            "address": fixture.order.address,
            "address_2": fixture.order.address_2,
            "price": fixture.order.price,
        }
    ]

    assert response.status_code == 200
    assert json.loads(response.content) == expected_json

