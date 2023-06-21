#!/usr/bin/python3
"""this module has route /status
"""
from models import storage
from models.farmer import Farmer
from models.buyer import Buyer
from models.product import Product
from models.order import Order
from models.review import Review
from flask import Flask, jsonify
from api.v1.views import app_views


farmer_ = storage.count(Farmer)
buyer_ = storage.count(Buyer)
product_ = storage.count(Product)
order_ = storage.count(Order)
review_ = storage.count(Review)


data = {"farmer": farmer_,
        "buyer": buyer_,
        "product": product_,
        "order": order_,
        "review": review_
        }


@app_views.route('/status', strict_slashes=False)
def return_json():
    """return a JSON: 'status': 'OK'"""
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route('/stats', strict_slashes=False)
def obj_no():
    """retrieves the number of each objects by type"""
    return jsonify(data)
