import json

from .utils import convert_to_dot_notation


def test_get_ordered_view_list(api_client, order_item):
    fixture = convert_to_dot_notation(order_item)

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
