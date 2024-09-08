from flask import Blueprint

product_routes = Blueprint("products", __name__, url_prefix='/products', static_folder='static', template_folder='templates')
from app.products.products import *