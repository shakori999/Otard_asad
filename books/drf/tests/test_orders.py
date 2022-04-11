import json

from .utils import convert_to_dot_notation


def test_get_ordered_view_list(api_client, ordered_order):
    fixture = convert_to_dot_notation(ordered_order)

    endpoint = f"/api/order/ordered-view/"
    response = api_client().get(endpoint)

    expected_json = [
        {
            "ordered_date": fixture.order.ordered_date,
            "name": fixture.order.name,
            "phone_number": fixture.order.phone_number,
            "price": fixture.order.price,
            "address": fixture.order.address,
            "address_2": fixture.order.address_2,
        }
    ]

    assert response.status_code == 200
    assert json.loads(response.content) == expected_json


def test_get_order_summary(api_client, order_item):
    fixture = convert_to_dot_notation(order_item)

    endpoint = f"/api/order/order-summary/"
    response = api_client().get(endpoint)

    expected_json = [
        {
            "items": [
                {
                    "item_name": fixture.order_item.item.product.name,
                    "quantity": fixture.order_item.quantity,
                    "individual_price": fixture.order_item.item.store_price,
                    "total_price": fixture.order_item.price,
                },
            ],
            "order_total_price": fixture.order.price,
        }
    ]

    print(expected_json)
    print(json.loads(response.content))
    assert response.status_code == 200
    assert json.loads(response.content) == expected_json
