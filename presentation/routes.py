from flask import Blueprint, jsonify, request
from data.database import DatabaseRepository

products_bp = Blueprint("products", __name__)

@products_bp.route("/products", methods=["GET"])
def get_products():
    repository = DatabaseRepository()
    products = repository.fetch_all("SELECT * FROM products")
    return jsonify(products)
