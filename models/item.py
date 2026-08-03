from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Item(db.Model):
    """
    Item Entity
    """

    __tablename__ = "items"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }

    def __repr__(self):

        return f"<Item {self.id} - {self.name}>"