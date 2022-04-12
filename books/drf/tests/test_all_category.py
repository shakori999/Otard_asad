def test_get_all_categories(api_client, category_with_multiple_children):
    endpoint = "/api/inventory/category/"
    response = api_client().get(endpoint)
    print(response.data)
    print(category_with_multiple_children)
    assert response.status_code == 200
    assert len(response.data) == len(category_with_multiple_children)
