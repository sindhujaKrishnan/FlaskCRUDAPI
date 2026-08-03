import logging

from models.item import db


logger = logging.getLogger(__name__)


class BaseRepository:

    def __init__(self, model):

        self.model = model


    # =========================================
    # GET ALL
    # =========================================

    def get_all(self):

        logger.debug(
            "Retrieving all records for model=%s",
            self.model.__name__
        )

        return self.model.query.all()


    # =========================================
    # GET BY ID
    # =========================================

    def get_by_id(self, entity_id):

        logger.debug(
            "Retrieving model=%s id=%s",
            self.model.__name__,
            entity_id
        )

        return db.session.get(
            self.model,
            entity_id
        )


    # =========================================
    # ADD
    # =========================================

    def add(self, entity):

        logger.debug(
            "Adding entity model=%s",
            self.model.__name__
        )

        db.session.add(entity)


    # =========================================
    # DELETE
    # =========================================

    def delete(self, entity):

        logger.debug(
            "Deleting entity model=%s",
            self.model.__name__
        )

        db.session.delete(entity)


    # =========================================
    # COMMIT
    # =========================================

    def commit(self):

        logger.debug(
            "Committing database transaction"
        )

        db.session.commit()


    # =========================================
    # ROLLBACK
    # =========================================

    def rollback(self):

        logger.warning(
            "Rolling back database transaction"
        )

        db.session.rollback()


    # =========================================
    # FLUSH
    # =========================================

    def flush(self):

        logger.debug(
            "Flushing database session"
        )

        db.session.flush()


    # =========================================
    # REFRESH
    # =========================================

    def refresh(self, entity):

        logger.debug(
            "Refreshing entity model=%s",
            self.model.__name__
        )

        db.session.refresh(entity)