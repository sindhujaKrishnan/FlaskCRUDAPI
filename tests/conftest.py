import pytest

from app import create_app
from config import TestConfig
from models.item import db, Item


# ===========================================
# Flask Test Application
# ===========================================

@pytest.fixture
def test_app():

    app = create_app(TestConfig)

    with app.app_context():

        db.create_all()

        yield app

        db.session.remove()

        db.drop_all()


# ===========================================
# Flask Test Client
# ===========================================

@pytest.fixture
def client(test_app):

    return test_app.test_client()


# ===========================================
# Sample Database Records
# ===========================================

@pytest.fixture
def sample_items(test_app):

    item1 = Item(
        name="Laptop",
        price=65000
    )

    item2 = Item(
        name="Mouse",
        price=800
    )

    item3 = Item(
        name="Keyboard",
        price=1500
    )

    db.session.add_all([
        item1,
        item2,
        item3
    ])

    db.session.commit()

    return [
        item1,
        item2,
        item3
    ]