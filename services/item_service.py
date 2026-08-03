import logging

from sqlalchemy.exc import SQLAlchemyError

from models.item import Item
from repositories.item_repository import ItemRepository
from utils.response import success, error
from utils.validators import validate_item


logger = logging.getLogger(__name__)


class ItemService:

    repository = ItemRepository()


    # =========================================
    # Get All Items
    # =========================================

    @classmethod
    def get_all_items(cls):

        try:

            logger.info(
                "Retrieving all items"
            )

            items = (
                cls.repository
                .get_all_ordered()
            )

            logger.info(
                "Retrieved %s items",
                len(items)
            )

            return success(
                message="Items retrieved successfully.",
                data=[
                    item.to_dict()
                    for item in items
                ]
            )

        except SQLAlchemyError:

            logger.exception(
                "Database error while retrieving items"
            )

            return error(
                message="Failed to retrieve items.",
                status_code=500
            )


    # =========================================
    # Get Item
    # =========================================

    @classmethod
    def get_item(cls, item_id):

        try:

            logger.info(
                "Retrieving item id=%s",
                item_id
            )

            item = (
                cls.repository
                .get_by_id(item_id)
            )

            if item is None:

                logger.warning(
                    "Item not found id=%s",
                    item_id
                )

                return error(
                    message=(
                        f"Item with Id "
                        f"{item_id} not found."
                    ),
                    status_code=404
                )

            return success(
                message="Item retrieved successfully.",
                data=item.to_dict()
            )

        except SQLAlchemyError:

            logger.exception(
                "Database error retrieving item id=%s",
                item_id
            )

            return error(
                message="Failed to retrieve item.",
                status_code=500
            )


    # =========================================
    # Add Item
    # =========================================

    @classmethod
    def add_item(cls, data):

        validate_item(data)

        try:

            logger.info(
                "Creating item name=%s",
                data["name"]
            )

            item = Item(
                name=data["name"].strip(),
                price=float(data["price"])
            )

            cls.repository.add(item)

            cls.repository.commit()

            logger.info(
                "Item created successfully id=%s",
                item.id
            )

            return success(
                message="Item added successfully.",
                data=item.to_dict(),
                status_code=201
            )

        except SQLAlchemyError:

            cls.repository.rollback()

            logger.exception(
                "Database error while adding item"
            )

            return error(
                message="Failed to add item.",
                status_code=500
            )


    # =========================================
    # Update Item
    # =========================================

    @classmethod
    def update_item(
        cls,
        item_id,
        data
    ):

        validate_item(data)

        try:

            logger.info(
                "Updating item id=%s",
                item_id
            )

            item = (
                cls.repository
                .get_by_id(item_id)
            )

            if item is None:

                logger.warning(
                    "Cannot update. Item not found id=%s",
                    item_id
                )

                return error(
                    message=(
                        f"Item with Id "
                        f"{item_id} not found."
                    ),
                    status_code=404
                )

            item.name = data["name"].strip()

            item.price = float(
                data["price"]
            )

            cls.repository.commit()

            logger.info(
                "Item updated successfully id=%s",
                item_id
            )

            return success(
                message="Item updated successfully.",
                data=item.to_dict()
            )

        except SQLAlchemyError:

            cls.repository.rollback()

            logger.exception(
                "Database error updating item id=%s",
                item_id
            )

            return error(
                message="Failed to update item.",
                status_code=500
            )


    # =========================================
    # Delete Item
    # =========================================

    @classmethod
    def delete_item(cls, item_id):

        try:

            logger.info(
                "Deleting item id=%s",
                item_id
            )

            item = (
                cls.repository
                .get_by_id(item_id)
            )

            if item is None:

                logger.warning(
                    "Cannot delete. Item not found id=%s",
                    item_id
                )

                return error(
                    message=(
                        f"Item with Id "
                        f"{item_id} not found."
                    ),
                    status_code=404
                )

            cls.repository.delete(item)

            cls.repository.commit()

            logger.info(
                "Item deleted successfully id=%s",
                item_id
            )

            return success(
                message="Item deleted successfully."
            )

        except SQLAlchemyError:

            cls.repository.rollback()

            logger.exception(
                "Database error deleting item id=%s",
                item_id
            )

            return error(
                message="Failed to delete item.",
                status_code=500
            )