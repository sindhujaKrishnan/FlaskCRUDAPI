import logging

from models.item import Item
from repositories.base_repository import BaseRepository


logger = logging.getLogger(__name__)


class ItemRepository(BaseRepository):

    def __init__(self):

        super().__init__(Item)


    # =========================================
    # Find By Name
    # =========================================

    def find_by_name(self, name):

        logger.debug(
            "Finding item by name=%s",
            name
        )

        return Item.query.filter_by(
            name=name
        ).first()


    # =========================================
    # Search By Name
    # =========================================

    def search_by_name(self, keyword):

        logger.debug(
            "Searching items keyword=%s",
            keyword
        )

        return Item.query.filter(
            Item.name.ilike(
                f"%{keyword}%"
            )
        ).all()


    # =========================================
    # Exists
    # =========================================

    def exists(self, item_id):

        logger.debug(
            "Checking item existence id=%s",
            item_id
        )

        return (
            self.get_by_id(item_id)
            is not None
        )


    # =========================================
    # Get All Ordered
    # =========================================

    def get_all_ordered(self):

        logger.debug(
            "Retrieving all items ordered by id"
        )

        return Item.query.order_by(
            Item.id
        ).all()