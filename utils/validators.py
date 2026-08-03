class ValidationException(Exception):
    """
    Custom Exception for Validation Errors
    """
    pass


def validate_item(data):
    """
    Validate Item Request
    """

    if data is None:
        raise ValidationException("Request body cannot be empty.")

    # Validate Name
    if "name" not in data:
        raise ValidationException("Item name is required.")

    if not isinstance(data["name"], str):
        raise ValidationException("Item name must be a string.")

    if data["name"].strip() == "":
        raise ValidationException("Item name cannot be empty.")

    # Validate Price
    if "price" not in data:
        raise ValidationException("Price is required.")

    try:
        price = float(data["price"])

        if price < 0:
            raise ValidationException("Price cannot be negative.")

    except ValueError:
        raise ValidationException("Price must be numeric.")