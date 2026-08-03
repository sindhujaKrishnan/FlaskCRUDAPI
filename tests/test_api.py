def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200


def test_get_all_items(
    client,
    sample_items
):

    response = client.get(
        "/items"
    )

    data = response.get_json()

    assert response.status_code == 200

    assert data["status"] == "success"

    assert len(data["data"]) == 3


def test_get_item(
    client,
    sample_items
):

    item_id = sample_items[0].id

    response = client.get(
        f"/items/{item_id}"
    )

    data = response.get_json()

    assert response.status_code == 200

    assert (
        data["data"]["name"]
        == "Laptop"
    )


def test_get_item_not_found(client):

    response = client.get(
        "/items/999"
    )

    data = response.get_json()

    assert response.status_code == 404
    assert data["status"] == "error"


def test_add_item(client):

    payload = {
        "name": "Monitor",
        "price": 15000
    }

    response = client.post(
        "/items",
        json=payload
    )

    data = response.get_json()

    assert response.status_code == 201

    assert data["status"] == "success"

    assert (
        data["data"]["name"]
        == "Monitor"
    )

    assert (
        data["data"]["price"]
        == 15000
    )


def test_add_item_without_name(client):

    payload = {
        "price": 15000
    }

    response = client.post(
        "/items",
        json=payload
    )

    data = response.get_json()

    assert response.status_code == 400

    assert data["status"] == "error"

    assert (
        data["message"]
        == "Item name is required."
    )


def test_add_item_invalid_price(client):

    payload = {
        "name": "Monitor",
        "price": "ABC"
    }

    response = client.post(
        "/items",
        json=payload
    )

    data = response.get_json()

    assert response.status_code == 400

    assert (
        data["message"]
        == "Price must be numeric."
    )


def test_update_item(
    client,
    sample_items
):

    item_id = sample_items[0].id

    payload = {
        "name": "Gaming Laptop",
        "price": 75000
    }

    response = client.put(
        f"/items/{item_id}",
        json=payload
    )

    data = response.get_json()

    assert response.status_code == 200

    assert (
        data["data"]["name"]
        == "Gaming Laptop"
    )

    assert (
        data["data"]["price"]
        == 75000
    )


def test_update_item_not_found(client):

    payload = {
        "name": "Laptop",
        "price": 65000
    }

    response = client.put(
        "/items/999",
        json=payload
    )

    data = response.get_json()

    assert response.status_code == 404
    assert data["status"] == "error"


def test_delete_item(
    client,
    sample_items
):

    item_id = sample_items[0].id

    response = client.delete(
        f"/items/{item_id}"
    )

    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"

    # Confirm it was actually deleted

    response = client.get(
        f"/items/{item_id}"
    )

    assert response.status_code == 404


def test_delete_item_not_found(client):

    response = client.delete(
        "/items/999"
    )

    data = response.get_json()

    assert response.status_code == 404
    assert data["status"] == "error"


def test_endpoint_not_found(client):

    response = client.get(
        "/invalid-endpoint"
    )

    data = response.get_json()

    assert response.status_code == 404

    assert (
        data["message"]
        == "API Endpoint Not Found."
    )


def test_method_not_allowed(client):

    response = client.patch(
        "/items"
    )

    data = response.get_json()

    assert response.status_code == 405

    assert (
        data["message"]
        == "HTTP Method Not Allowed."
    )


def test_request_id_header(client):

    response = client.get(
        "/items"
    )

    assert "X-Request-ID" in response.headers

    assert response.headers[
        "X-Request-ID"
    ]