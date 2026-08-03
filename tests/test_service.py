from services.item_service import ItemService


def test_get_all_items(
    test_app,
    sample_items
):

    response, status_code = (
        ItemService.get_all_items()
    )

    data = response.get_json()

    assert status_code == 200
    assert data["status"] == "success"
    assert len(data["data"]) == 3


def test_get_item(
    test_app,
    sample_items
):

    item_id = sample_items[0].id

    response, status_code = (
        ItemService.get_item(item_id)
    )

    data = response.get_json()

    assert status_code == 200
    assert data["status"] == "success"
    assert data["data"]["name"] == "Laptop"


def test_get_item_not_found(
    test_app
):

    response, status_code = (
        ItemService.get_item(999)
    )

    data = response.get_json()

    assert status_code == 404
    assert data["status"] == "error"


def test_add_item(test_app):

    item_data = {
        "name": "Monitor",
        "price": 15000
    }

    response, status_code = (
        ItemService.add_item(
            item_data
        )
    )

    data = response.get_json()

    assert status_code == 201

    assert data["status"] == "success"

    assert (
        data["data"]["name"]
        == "Monitor"
    )

    assert (
        data["data"]["price"]
        == 15000
    )


def test_update_item(
    test_app,
    sample_items
):

    item_id = sample_items[0].id

    update_data = {
        "name": "Gaming Laptop",
        "price": 75000
    }

    response, status_code = (
        ItemService.update_item(
            item_id,
            update_data
        )
    )

    data = response.get_json()

    assert status_code == 200

    assert (
        data["data"]["name"]
        == "Gaming Laptop"
    )

    assert (
        data["data"]["price"]
        == 75000
    )


def test_update_item_not_found(
    test_app
):

    update_data = {
        "name": "Laptop",
        "price": 65000
    }

    response, status_code = (
        ItemService.update_item(
            999,
            update_data
        )
    )

    data = response.get_json()

    assert status_code == 404
    assert data["status"] == "error"


def test_delete_item(
    test_app,
    sample_items
):

    item_id = sample_items[0].id

    response, status_code = (
        ItemService.delete_item(
            item_id
        )
    )

    data = response.get_json()

    assert status_code == 200
    assert data["status"] == "success"


def test_delete_item_not_found(
    test_app
):

    response, status_code = (
        ItemService.delete_item(
            999
        )
    )

    data = response.get_json()

    assert status_code == 404
    assert data["status"] == "error"