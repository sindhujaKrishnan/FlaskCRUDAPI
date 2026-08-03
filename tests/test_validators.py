import pytest

from utils.validators import validate_item, ValidationException


def test_validate_valid_item():

    data = {
        "name": "Laptop",
        "price": 65000
    }

    validate_item(data)


def test_validate_none_request_body():

    with pytest.raises(
        ValidationException,
        match="Request body cannot be empty."
    ):

        validate_item(None)


def test_validate_name_missing():

    data = {
        "price": 65000
    }

    with pytest.raises(
        ValidationException,
        match="Item name is required."
    ):

        validate_item(data)


def test_validate_name_empty():

    data = {
        "name": "",
        "price": 65000
    }

    with pytest.raises(
        ValidationException,
        match="Item name cannot be empty."
    ):

        validate_item(data)


def test_validate_name_spaces_only():

    data = {
        "name": "   ",
        "price": 65000
    }

    with pytest.raises(
        ValidationException,
        match="Item name cannot be empty."
    ):

        validate_item(data)


def test_validate_name_not_string():

    data = {
        "name": 123,
        "price": 65000
    }

    with pytest.raises(
        ValidationException,
        match="Item name must be a string."
    ):

        validate_item(data)


def test_validate_price_missing():

    data = {
        "name": "Laptop"
    }

    with pytest.raises(
        ValidationException,
        match="Price is required."
    ):

        validate_item(data)


def test_validate_price_not_numeric():

    data = {
        "name": "Laptop",
        "price": "ABC"
    }

    with pytest.raises(
        ValidationException,
        match="Price must be numeric."
    ):

        validate_item(data)


def test_validate_negative_price():

    data = {
        "name": "Laptop",
        "price": -100
    }

    with pytest.raises(
        ValidationException,
        match="Price cannot be negative."
    ):

        validate_item(data)


def test_validate_zero_price():

    data = {
        "name": "Free Item",
        "price": 0
    }

    validate_item(data)


def test_validate_numeric_string_price():

    data = {
        "name": "Mouse",
        "price": "800"
    }

    validate_item(data)