from flask import jsonify


def success(message, data=None, status_code=200):
    """
    Standard Success Response
    """

    response = {
        "status": "success",
        "message": message,
        "data": data
    }

    return jsonify(response), status_code


def error(message, status_code=400, errors=None):
    """
    Standard Error Response
    """

    response = {
        "status": "error",
        "message": message
    }

    if errors is not None:
        response["errors"] = errors

    return jsonify(response), status_code