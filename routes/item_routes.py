from flask import Blueprint, request, render_template
from services.item_service import ItemService

item_bp = Blueprint("item_bp", __name__)


@item_bp.route("/")
def home():
    return render_template("index.html")


@item_bp.route("/items", methods=["GET"])
def get_all_items():
    return ItemService.get_all_items()


@item_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    return ItemService.get_item(item_id)


@item_bp.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    return ItemService.add_item(data)


@item_bp.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    return ItemService.update_item(item_id, data)


@item_bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    return ItemService.delete_item(item_id)