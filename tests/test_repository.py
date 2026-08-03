from models.item import Item
from repositories.item_repository import ItemRepository


def test_add_item(test_app):

    repository = ItemRepository()

    item = Item(
        name="Laptop",
        price=65000
    )

    repository.add(item)
    repository.commit()

    assert item.id is not None

    saved_item = repository.get_by_id(item.id)

    assert saved_item is not None
    assert saved_item.name == "Laptop"
    assert saved_item.price == 65000


def test_get_all_items(
    test_app,
    sample_items
):

    repository = ItemRepository()

    items = repository.get_all()

    assert len(items) == 3


def test_get_all_ordered(
    test_app,
    sample_items
):

    repository = ItemRepository()

    items = repository.get_all_ordered()

    assert len(items) == 3

    assert items[0].id < items[1].id
    assert items[1].id < items[2].id


def test_get_item_by_id(
    test_app,
    sample_items
):

    repository = ItemRepository()

    item_id = sample_items[0].id

    item = repository.get_by_id(
        item_id
    )

    assert item is not None
    assert item.name == "Laptop"
    assert item.price == 65000


def test_get_non_existing_item(
    test_app
):

    repository = ItemRepository()

    item = repository.get_by_id(
        999
    )

    assert item is None


def test_find_by_name(
    test_app,
    sample_items
):

    repository = ItemRepository()

    item = repository.find_by_name(
        "Laptop"
    )

    assert item is not None
    assert item.name == "Laptop"


def test_search_by_name(
    test_app,
    sample_items
):

    repository = ItemRepository()

    items = repository.search_by_name(
        "key"
    )

    assert len(items) == 1
    assert items[0].name == "Keyboard"


def test_search_by_name_case_insensitive(
    test_app,
    sample_items
):

    repository = ItemRepository()

    items = repository.search_by_name(
        "LAP"
    )

    assert len(items) == 1
    assert items[0].name == "Laptop"


def test_item_exists(
    test_app,
    sample_items
):

    repository = ItemRepository()

    item_id = sample_items[0].id

    assert repository.exists(
        item_id
    ) is True


def test_item_does_not_exist(
    test_app
):

    repository = ItemRepository()

    assert repository.exists(
        999
    ) is False


def test_update_item(
    test_app,
    sample_items
):

    repository = ItemRepository()

    item = sample_items[0]

    item.name = "Gaming Laptop"
    item.price = 75000

    repository.commit()

    updated_item = repository.get_by_id(
        item.id
    )

    assert updated_item.name == "Gaming Laptop"
    assert updated_item.price == 75000


def test_delete_item(
    test_app,
    sample_items
):

    repository = ItemRepository()

    item = sample_items[0]

    item_id = item.id

    repository.delete(item)
    repository.commit()

    deleted_item = repository.get_by_id(
        item_id
    )

    assert deleted_item is None